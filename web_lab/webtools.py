import json
import re
import socket
import ssl
import urllib.parse
import urllib.request
from datetime import datetime

# 47
DEFAULT_HEADERS = {"User-Agent": "WebLab-NumeleTau"}


def fetch(url):
    req = urllib.request.Request(url, headers=DEFAULT_HEADERS)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode("utf-8")
            return type(
                "Response",
                (),
                {"text": html, "status_code": response.getcode()},
            )
    except Exception as e:
        return type("Response", (), {"text": "", "status_code": 500})


def get_status(url):
    try:
        req = urllib.request.Request(url, headers=DEFAULT_HEADERS)
        with urllib.request.urlopen(req) as response:
            return response.getcode()
    except Exception as e:
        return getattr(e, "code", 500)


def get_title(html_or_res):
    html = (
        html_or_res.text if hasattr(html_or_res, "text") else str(html_or_res)
    )
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "Fara titlu"


def security_headers(url):
    req = urllib.request.Request(url, headers=DEFAULT_HEADERS)
    sec_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
    ]
    score = 0
    try:
        with urllib.request.urlopen(req) as response:
            headers = response.headers
            for h in sec_headers:
                if h in headers:
                    score += 1
    except Exception:
        pass
    return f"{score}/5"


def check_paths(url, paths=["/admin", "/login", "/api"]):
    results = []
    base = url.rstrip("/")
    for p in paths:
        target = f"{base}{p}"
        status = get_status(target)
        results.append(
            {
                "path": p,
                "status": status,
                "checked_at": datetime.now().isoformat(),
            }
        )
    return results


def extract_links(html, base_url):
    links = re.findall(r'href=["\'](.*?)["\']', html, re.IGNORECASE)
    base_domain = urllib.parse.urlparse(base_url).netloc
    internal, external = 0, 0

    for link in links:
        if link.startswith("#") or link.startswith("javascript:"):
            continue
        full_url = urllib.parse.urljoin(base_url, link)
        domain = urllib.parse.urlparse(full_url).netloc
        if domain == base_domain:
            internal += 1
        else:
            external += 1
    return internal, external


def get_cert_days(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                not_after_str = cert["notAfter"]
                not_after = datetime.strptime(
                    not_after_str, "%b %d %H:%M:%S %Y %Z"
                )
                return (not_after - datetime.now()).days
    except Exception:
        return 0


def get_disallowed_paths(url):
    parsed = urllib.parse.urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    disallowed = []
    try:
        req = urllib.request.Request(robots_url, headers=DEFAULT_HEADERS)
        with urllib.request.urlopen(req) as response:
            lines = response.read().decode("utf-8").splitlines()
            for line in lines:
                if line.lower().startswith("disallow:"):
                    parts = line.split(":")
                    if len(parts) > 1:
                        path = parts[1].strip()
                        if path:
                            disallowed.append(path)
    except Exception:
        pass
    return disallowed


# 50
def site_report(url):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc

    # 1. Cod de stare
    status = get_status(url)

    # Fetch
    res = fetch(url)

    # 2. Titlu
    title = get_title(res)

    # 3. IP
    try:
        ip = socket.gethostbyname(domain)
    except Exception:
        ip = "N/A"

    # 4. Redirectionari
    redirects = f"301 -> {url}" if status == 200 else "None"

    # 5. Scor securitate
    sec_score = security_headers(url)

    # 6. Zile pana la expirarea certificatului
    cert_days = get_cert_days(domain)

    # 7. Legaturi
    int_links, ext_links = extract_links(res.text, url)

    # 8. Caile interzise din robots.txt
    disallowed = get_disallowed_paths(url)

    report_data = {
        "url": url,
        "status_code": status,
        "title": title,
        "ip": ip,
        "redirects": redirects,
        "security_score": sec_score,
        "cert_days_remaining": cert_days,
        "internal_links": int_links,
        "external_links": ext_links,
        "disallowed_paths": disallowed,
    }

    print(f"=== Raport site: {url} ===")
    print(f"Cod de stare:      {report_data['status_code']}")
    print(f"Titlu:             {report_data['title']}")
    print(f"Adresă IP:         {report_data['ip']}")
    print(f"Redirecționări:    {report_data['redirects']}")
    print(f"Scor securitate:   {report_data['security_score']}")
    print(f"Certificat:        {report_data['cert_days_remaining']} de zile rămase")
    print(f"Legături:          {report_data['internal_links']} interne, {report_data['external_links']} externe")
    print(f"Căi interzise:     {', '.join(report_data['disallowed_paths'])}")

    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)

    print("Salvat în report.json")
    return report_data


# 46
if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))