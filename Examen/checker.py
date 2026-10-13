import requests

SITES = [
    # Pagini obișnuite (Părțile 2, 3 și 4)
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    # Pagini care eșuează
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    # Anteturi de securitate (Partea 5)
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    # Răspunde aleatoriu cu 200 sau 500 (Partea 6)
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]


def build_url(host, path):
    """Returnează o adresă completă, de exemplu https://example.com/login."""
    if path.startswith("/"):
        build = host + path
    else: build = host + "/" + path
    return build

# print(build_url("https://example.com", "/path"))
# print(build_url("https://example.com", "path"))



def is_https(url):
    """Returnează True dacă adresa începe cu https://, altfel False."""
    if url.startswith("https://"):
        return True
    else : return False

# print(is_https("https://example.com"))
# print(is_https("http://example.com"))


def show_response(url):
    """Trimite un GET la url și afișează statusul și Content-Type."""
    r = requests.get(url)
    return r.status_code, r.headers['content-type']

# print(show_response("https://example.com"))


def check_site(url):
    """Returnează un dicționar cu: status, content_type, length, server."""
    r = requests.get(url, timeout=5)
    d = {
        "status" : r.status_code,
        "content_type" : r.headers['content-type'],
        "length" : len(r.content),
        "server" : r.headers['server']
    }
    return d

# print(check_site("https://example.com"))


def scan_sites():
    """Verifică toate site-urile din SITES, afișează-le pe cele care merg și un rezumat."""
    pass


def check_headers(url):
    """Returnează un dicționar cu: present, missing, score."""
    response = requests.get(url, timeout=5)
    present = []
    missing = []
    for header in SECURITY_HEADERS:
        if header in response.headers:
            present.append(header)
        else:
            missing.append(header)
    scor = len(present) / len(SECURITY_HEADERS) * 100
    return {"present": present, "missing": missing, "scor": scor}

# print(check_headers("https://example.com"))




def retry_check(url, attempts=3):
    """Încearcă de cel mult `attempts` ori; returnează un dicționar cu: status, attempts."""
    for i in range(attempts):
        try:
            response = requests.get(url, timeout=5)
            return {"status": response.status_code, "attempts": i+1}
        except requests.RequestException:
            continue
    return {"status": None, "attempts": attempts}

# print(retry_check("https://example.com", 5))

