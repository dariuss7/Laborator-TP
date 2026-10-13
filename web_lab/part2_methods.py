# Laborator: funcții, metode și importuri pe web
# Student: Maister Darius
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


import requests
import urllib.request
import time


#9
response = requests.get(BASE_URL, timeout=TIMEOUT) # metoda

# print(response.status_code) #atribut
# print(response.ok) # atribut
# print(response.url) # atribut
# print(response.encoding) # atribut



#10



# response.raise_for_status()

# try:
#     requests.get(BASE_URL + "/this-page-does-not-exist", timeout=TIMEOUT)
# except requests.HTTPError:
#     print("this page does not exist")


#11

# for name,value in response.headers.items(): 
    # print(f"{name}: {value}")


#12

# server = response.headers.get("Server", "lipseste")
# time.sleep(1)
# content = response.headers.get("Content-Type", "lipseste")
# print(f"Server: {server}")
# print(f"Content-Type: {content}")
# time.sleep(1)
# content_lower = response.headers.get("content-type", "lipseste")
# print(f"content-type: {content_lower}")

# ambele metode returneaza aceeasi valoare legata de content-type, doarece requests.headers este case-insensitive, 
# adica numele antetelor nu tin cont de litere mari/mici



#13

# print(response.text.lower().count("cyber"))
# ambele metode sunt de tip string respectiv pot fi executate secvential, de la stanga la dreapta
# lower() transforma string-ul textului paginii in acelasi text la lower case, si respectiv este tot string si poate fi folost count() pentru a numara
# aparitiile argumentului "cyber"


#14

# html = response.text
# start = html.find("<title>") + len("<text>")
# end = html.find("</title>")
# title = html[start:end].strip()
# print(title)

#15

# html = response.text
# lines = html.splitlines()
# lunga = max(lines, key=len)


# print(f"numarul de linii: {len(lines)}")
# print(f"cea mai lunga linie: {lunga}")
# print(f"si lungimea ei: {len(lunga)}")


#16

# if response.url.startswith("https://"): print("Conexiune securizata")
# else : print("Conexiune nesecurizata")


#17

# cerere = requests.get("http://cybercor.org", timeout=TIMEOUT)

# for r in cerere.history:
#     print(f"{r.status_code} - {r.url}")


# print(cerere.url)

#301 - moved permanently


#18

# response2 = requests.head(BASE_URL, timeout=TIMEOUT)

# print(len(response.content))
# print(len(response2.content))

# head extrage doar antetele, dar get extrage si antetele si continutul/body-ul(response.text) al paginii, 
# respectiv len al response2 este 0 deoarece head nu a extras body-ul html, iar response1 va da lungimea textului din body


#19

# if response.cookies:

#     for c in response.cookies:
#         print(f"Name: {c.name}, Secure: {c.secure}")

# else: print("Niciun cookie gasit")


#20
# session = requests.Session()
# session.headers.update({"User-Agent": f"WebLab-Darius"})
# cerere = session.get(ECHO_URL  + "/headers", timeout=TIMEOUT)
# print(cerere.text)


#reponse.text este corpul paginii descarcat ca string,dar response.json() este o functie care proceseaza datele

















