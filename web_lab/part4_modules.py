# Laborator: funcții, metode și importuri pe web
# Student: Maister Darius
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


import requests
import urllib.request
import time
import urllib.parse
import re
import html.parser
import hashlib
import json
import socket
import ssl
import datetime



#35

# response = urllib.parse.urlparse(BASE_URL + "/path?x=1#top")

# print(response.scheme)
# print(response.netloc)
# print(response.path)
# print(response.query)
# print(response.fragment)


#36

# relatives = ['/about', 'contact.html', '../index.html']

# for r in relatives:
#     full_url = response = urllib.parse.urljoin(BASE_URL, r)
#     print(full_url)



#37


# from urllib.parse import urljoin
# def extract_links(html, base_url):
#     raw_links = re.findall(r'href="([^"]+)"', html)
#     full_links = [urljoin(base_url, link) for link in raw_links]
#     return list(dict.fromkeys(full_links))

# response = requests.get(BASE_URL, timeout=5)

# links = extract_links(response.text, BASE_URL)

# for link in links[:10]:
#     print(link)


#38

# from urllib.parse import urljoin, urlparse

# def extract_links(html, base_url):
#     raw_links = re.findall(r'href="([^"]+)"', html)
#     full_links = [urljoin(base_url, link) for link in raw_links]
#     return list(dict.fromkeys(full_links))

# response = requests.get(BASE_URL, timeout=5)

# links = extract_links(response.text, BASE_URL)
# for link in links[:10]:
#     print(link)


#39

# from html.parser import HTMLParser


# class ImageFinder(HTMLParser):

#     def __init__(self):
#         super().__init__()
#         self.images = []

#     def handle_starttag(self, tag, attrs):
#         if tag == "img":
#             src = dict(attrs).get("src")
#             if src:
#                 self.images.append(src)


# test_html = """
# <html><body>
#   <img src="/logo.png" alt="Logo">
#   <IMG SRC="poza.jpg">
#   <img alt="imagine fără src">
#   <img src="https://cdn.example.com/banner.webp" />
#   <a href="/despre">Aceasta nu este o imagine</a>
# </body></html>
# """
 
# finder = ImageFinder()
# finder.feed(test_html)
# print(finder.images)
 
# assert finder.images == [
#     "/logo.png",                            # imagine obișnuită
#     "poza.jpg",                             # tag scris cu majuscule
#     "https://cdn.example.com/banner.webp",  # tag care se închide singur
# ], "Parserul nu a găsit exact imaginile așteptate"
# print("Testul a trecut!")


# response = requests.get(BASE_URL, timeout=TIMEOUT)

# finder = ImageFinder()
# finder.feed(response.text)
# print(len(finder.images), "imagini găsite")
# for src in finder.images:
#     print(src)

# print(response.text.lower().count("<img") )


#40

# def page_fingerprint(url):
#     response = requests.get(url,timeout=TIMEOUT)
#     return hashlib.sha256(response.content).hexdigest()


# hash1 = page_fingerprint(BASE_URL)
# hash2 = page_fingerprint(BASE_URL)

# print(hash1)
# print(hash2)

#Hash-urile SHA-256 vor fi diferite oricând conținutul brut al răspunsului HTTP (response.content) se modifică de la o cerere la alta, 
# chiar și printr-un singur caracter sau octeți


#41

# response = requests.get(BASE_URL)

# with open("headers.json", "w", encoding="utf-8") as file:
#     json.dump(dict(response.headers), file, indent=2)

# print("Antetele au fost salvate cu succes în headers.json!\n")

# with open("headers.json", "r", encoding="utf-8") as file:
#     loaded_headers = json.load(file)

# header_key = "Content-Type"
# print(f"{header_key}: {loaded_headers.get(header_key)}")


#42

# def resolve(hostname):
#     print(socket.gethostbyname(hostname))

# resolve("cybercor.org")



#43

# import time
# import socket, ssl

# def cert_days_left(hostname):
#     context = ssl.create_default_context()
    
#     with socket.create_connection((hostname, 443)) as sock:
#         with context.wrap_socket(sock, server_hostname=hostname) as ssock:
#             cert = ssock.getpeercert()
    
#     expire_timestamp = ssl.cert_time_to_seconds(cert["notAfter"])
#     seconds_left = expire_timestamp - time.time()
#     return int(seconds_left // (24 * 3600))


# print(cert_days_left("cybercor.org"), "zile")


#Metoda handle_starttag() este apelată automat de către metoda feed() din clasa de bază HTMLParser


#44







