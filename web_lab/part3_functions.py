# Laborator: funcții, metode și importuri pe web
# Student: Maister Darius
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


import requests
import urllib.request
import time


#returneaza codul de stare http pentru o adresa url
def get_status(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code
    print(response.status_code)



#21

def fetch(url):  
    response = requests.get(url, timeout=TIMEOUT)
    return response

# response_obj = fetch(BASE_URL)
# print(response_obj.status_code)



#22

# def get_status(url):
#     response = requests.get(url, timeout=TIMEOUT)
#     print(response.status_code)


# get_status(BASE_URL + "/")
# time.sleep(1)
# get_status(BASE_URL + "/robots.txt")
# time.sleep(1)
# get_status(BASE_URL + "/sitemap.xml")


#23

# def get_status(url, timeout=10):
#     response = requests.get(url, timeout=TIMEOUT)
#     print(response.status_code)


# get_status(BASE_URL)
# get_status(BASE_URL, timeout=3)


#24




# def get_title(html):
#     start = html.find("<title>") + len("<text>")
#     end = html.find("</title>")
#     title = html[start:end].strip()
#     print(title)

# obj = fetch(BASE_URL)
# get_title(obj.text)


#25

# def get_title(html):

#     """extrage si afiseaza titlul unei pagini html din <title></title>
    
#     html este argumentul string ce reprezinta continutul paginii ca un sir de caractere"""

#     start = html.find("<title>") + len("<text>")
#     end = html.find("</title>")
#     title = html[start:end].strip()
#     print(title)


# help(get_title)


#26



# def fetch(url: str) -> requests.Response:
#     url_text = str(url)
#     if not url_text.startswith("http://") and not url_text.startswith(
#         "https://"
#     ):
#         url_text = "https://" + url_text

#     response = requests.get(url_text, timeout=TIMEOUT)
#     return response


# def get_status(url: str) -> int:
#     response = fetch(url)
#     return response.status_code

# status = get_status(123)
# print(status)

#adnotarile nu ne opresc deoarece au scop informativ si python nu le ia in considrare cand executa programul


#27

# def page_exists(url):
#     try:
#         requests.get(BASE_URL, timeout=TIMEOUT)
#         print("True")
#     except requests.RequestException: 
#         print("False")


# print(page_exists("https://this-domain-does-not-exist.invalid"))


#28

# def check_paths(base, paths):
#     results = {}
#     base_url = base.rstrip('/')
    
#     for path in paths:
#         formatted_path = path if path.startswith('/') else '/' + path
#         full_url = base_url + formatted_path
        
#         try:
#             response = requests.get(full_url, timeout=5)
#             results[path] = response.status_code
#         except requests.RequestException:
#             results[path] = None
            
#     return results



#29


# def get_header(url, name, default="lipsește"):
#     response = requests.head(url, timeout=5, allow_redirects=True)
#     return response.headers.get(name, default)

# get_header(BASE_URL, name="server")




#30

# def security_headers(url):

#     list_to_check =["Strict-Transport-Security",
#         "Content-Security-Policy",
#         "X-Frame-Options",
#         "X-Content-Type-Options",
#         "Referrer-Policy"
#     ]

#     response =requests.head(url, timeout=TIMEOUT)



#     for antet in list_to_check:
#         if antet in response.headers:
#             print(f"{antet}: True")
#         else: print(f"{antet}: False")

# security_headers(BASE_URL)


# A DOUA METODA

# def security_headers(url):
#     list_to_check = [
#         "Strict-Transport-Security",
#         "Content-Security-Policy",
#         "X-Frame-Options",
#         "X-Content-Type-Options",
#         "Referrer-Policy"
#     ]

#     response = requests.head(url, timeout=TIMEOUT)
#     results = {}

#     for antet in list_to_check:
#         results[antet] = antet in response.headers

#     return results


# #31

# def score_headers(results):
#     score = sum(results.values())
#     total = len(results)
#     return f"{score}/{total}"


# print(score_headers(security_headers(BASE_URL)))


# #32

# def fetch_robots(base):
#     url = base.rstrip('/') + '/robots.txt'
#     try:
#         response = requests.get(url, timeout=5)
#         if response.status_code == 200:
#             return response.text
#         return None
#     except requests.RequestException:
#         return None


# def disallowed_paths(robots_text):
#     if not robots_text:
#         return []
    
#     paths = []
#     for line in robots_text.splitlines():
#         line = line.strip()
#         if line.lower().startswith('disallow:'):
#             parts = line.split(':', 1)
#             if len(parts) > 1:
#                 path = parts[1].strip()
#                 if path:
#                     paths.append(path)
                    
#     return paths

# content = fetch_robots(BASE_URL)
# paths = disallowed_paths(content)
# print(paths)


#33


# def response_times(*urls):
#     results = {}
#     for url in urls:
#         response = requests.get(url, timeout=5)
#         results[url] = response.elapsed.total_seconds()
#     print(results)


# response_times(BASE_URL, ECHO_URL)



#34


# def log(message, **details):
#     items = [message]
#     for key, value in details.items():
#         items.append(f"{key}={value}")
#     print(" | ".join(items))

# log("verificat", url=BASE_URL, status=200)





# print() afișează date in consola. Valoarea afișată nu este salvată și nu poate fi folosită mai departe în cod
# return trimite o valoare înapoi în program: oprește execuția funcției și îi transmite rezultatul codului care a apelat-o. 
# această valoare poate fi salvată într-o variabilă, transmisă altei funcții sau folosită în calcule.



