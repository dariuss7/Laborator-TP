import requests
import time

BASE = "https://httpbin.org"
PATHS = ["/get", "/redirect/2", "/delay/1", "/status/404", "/delay/5"]


# Partea 1: parametri în URL

def search(params):
    # GET pe /get cu parametri în URL; returnează parametrii primiți de server.
    r = requests.get(BASE + "/get", params=params, timeout=5)
    return r.json()["args"]


def search_url(params):
    # Returnează adresa completă construită de requests, cu tot cu parametri.
    r = requests.get(BASE + "/get", params=params, timeout=5)
    return r.url


# Partea 2: anteturi

def fetch_with_agent(agent):
    # GET pe /headers cu User-Agent=agent.
    r = requests.get(
        BASE + "/headers",
        headers={"User-Agent": agent},
        timeout=5
    )
    return r.json()["headers"]["User-Agent"]


def default_agent():
    # Returnează User-Agent-ul trimis de requests când nu setezi nimic.
    r = requests.get(BASE + "/headers", timeout=5)
    return r.json()["headers"]["User-Agent"]


# Partea 3: trimiterea datelor

def post_json(data):
    # POST cu datele ca JSON.
    r = requests.post(BASE + "/post", json=data, timeout=5)
    return r.json()["json"]


def post_form(data):
    # POST cu datele ca formular.
    r = requests.post(BASE + "/post", data=data, timeout=5)
    return r.json()["form"]


# Partea 4: coduri de stare

def describe_status(code):
    r = requests.get(BASE + "/status/" + str(code), timeout=5)

    if 200 <= r.status_code < 300:
        return "succes"

    if 400 <= r.status_code < 500:
        return "eroare client"

    if 500 <= r.status_code < 600:
        return "eroare server"

    return "alt status"


def is_ok(code):
    r = requests.get(BASE + "/status/" + str(code), timeout=5)
    return r.ok


# Partea 5: redirecționări

def count_redirects(n):
    r = requests.get(BASE + "/redirect/" + str(n), timeout=5)
    return len(r.history)


def final_url(n):
    r = requests.get(BASE + "/redirect/" + str(n), timeout=5)
    return r.url


def first_hop(n):
    r = requests.get(
        BASE + "/redirect/" + str(n),
        allow_redirects=False,
        timeout=5
    )
    return r.headers.get("Location")


# Partea 6: sesiuni și cookie-uri

def cookie_demo(name, value):
    s = requests.Session()

    s.get(BASE + "/cookies/set/" + name + "/" + value, timeout=5)

    r = s.get(BASE + "/cookies", timeout=5)

    return r.json()["cookies"]


def no_session_demo(name, value):
    requests.get(
        BASE + "/cookies/set/" + name + "/" + value,
        timeout=5
    )

    r = requests.get(BASE + "/cookies", timeout=5)

    return r.json()["cookies"]


# Partea 7: raportul final

def report(path):
    start = time.perf_counter()

    try:
        r = requests.get(BASE + path, timeout=3)

        seconds = time.perf_counter() - start

        return {
            "status": r.status_code,
            "final_url": r.url,
            "redirects": len(r.history),
            "seconds": seconds,
            "content_type": r.headers.get("Content-Type")
        }

    except requests.RequestException:
        seconds = time.perf_counter() - start

        return {
            "status": None,
            "final_url": None,
            "redirects": 0,
            "seconds": seconds,
            "content_type": None
        }


# Bonus: autentificare

def check_login(user, password):
    try:
        r = requests.get(
            BASE + "/basic-auth/admin/secret",
            auth=(user, password),
            timeout=5
        )

        return r.status_code == 200

    except requests.RequestException:
        return False


def main():

    print("=== Partea 1 ===")
    print(search({"q": "python", "page": 2}))
    print(search_url({"q": "python", "page": 2}))

    print("\n=== Partea 2 ===")
    print(fetch_with_agent("WebLab-Darius"))
    print(default_agent())

    print("\n=== Partea 3 ===")
    print(post_json({"nume": "Darius", "grupa": "SI-262"}))
    print(post_form({"nume": "Darius", "grupa": "SI-262"}))

    print("\n=== Partea 4 ===")
    print(describe_status(200))
    print(describe_status(404))
    print(describe_status(500))
    print(is_ok(200))
    print(is_ok(404))

    print("\n=== Partea 5 ===")
    print("Redirectionari:", count_redirects(2))
    print("URL final:", final_url(2))
    print("Primul hop:", first_hop(2))

    print("\n=== Partea 6 ===")
    print("Cu sesiune:", cookie_demo("user", "Darius"))
    print("Fara sesiune:", no_session_demo("user", "Darius"))

    print("\n=== Partea 7 ===")
    for path in PATHS:
        print(path, report(path))

    print("\n=== Bonus ===")
    print("Login corect:", check_login("admin", "secret"))
    print("Login gresit:", check_login("admin", "gresit"))


if __name__ == "__main__":
    main()