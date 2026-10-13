# Laborator: funcții, metode și importuri pe web
# Student: Maister Darius
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


import requests
#print(requests.__version__)
import urllib.request
import time

#libraria requests a avut nevoie de "pip install", deoarece este o librarie Python standard
#urllib este o librarie care face parte din libraria python standard, respectiv este pre-instalata

#2
# print(requests.get(BASE_URL), timeout=TIMEOUT)

#from requests import get

# response = get(BASE_URL, timeout=TIMEOUT)

#print(response.status_code)

# un avantaj al primului stil este faptul ca nu vom incurca functia get() pe care o importam din requests cu o alta functie cu denumire similara
#un avantaj al stilului 2 este ca importam functia requests.get() ca get(), si putem apela direct get(), fara a mai scrie din nou denumirea modulului

#3


# import requests as rq
# print(rq.get(BASE_URL, timeout= TIMEOUT))

# un alias poate contribui la eliminarea confuziei cand importam module cu nume similare din pachete diferite
# un alias poate crea connfuzie cand dam aliasuri librariilor simple precum requests sau json, incat un programator trebuie sa verifice la inceputul codului
# obiectul utilizat

#4

# from urllib.request import urlopen


# with urlopen(BASE_URL, timeout=TIMEOUT) as response:
#     print("Status HTTP:", response.status)
    
#     # Citim corpul răspunsului, îl decodificăm din octeți (bytes) în text (utf-8)
#     body_text = response.read().decode("utf-8")
    
#     print("\nPrimele 200 de caractere din corp:")
#     print(body_text[:200])


#5

# print(dir(requests))

# # functie - get 
# # clasa - __file__
# # modul - status_codesS

#6

# from requests import get
# print(get(BASE_URL, timeout=3))



#7
# import time

# print(time.perf_counter())
# response = requests.get(BASE_URL, timeout=TIMEOUT)
# print(time.perf_counter())
# print(response.elapsed)

#8
# try:
#     import bs4
# except ImportError:
#         print("trebuie sa instalati modulul cu : pip install beautifulsoup4")




#un modul este un file .py care contine variabile, functii, clase. un pachet este un folder cu mai multe module, in care este inclus si un fisier __init__.py
# care indica faptul ca acel folder este un pachet. o biblioteca este o totalitate de pachete si module




