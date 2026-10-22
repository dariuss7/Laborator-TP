#A1

s = "Salut"
b = s.encode()          # bytes
print(b, b[0])          # b"Salut" 83

# TODO: tipareste b.hex() si refa bytes din hex
hex_str = b.hex()
print("Hex:", hex_str)

b_refacut = bytes.fromhex(hex_str)
print("Bytes refăcuți:", b_refacut)



#A2

import re

def ghici_strat(s):
    # Verificăm întâi URL (are secvențe %xx)
    if "%" in s and re.search(r"%[0-9a-fA-F]{2}", s):
        return "url"
    # Verificăm Hex (doar 0-9, a-f, A-F și lungime pară)
    if re.fullmatch(r"[0-9a-fA-F]+", s) and len(s) % 2 == 0:
        return "hex"
    # Verificăm Base64 (alfabet standard A-Z, a-z, 0-9, +, /, =)
    if re.fullmatch(r"[A-Za-z0-9+/=]+", s) and len(s) % 4 == 0:
        return "base64"
    return "necunoscut"

# Teste:
# print(ghici_strat("%2Fetc"))         # url
# print(ghici_strat("48656c6c6f"))     # hex
# print(ghici_strat("U2FsdXQ="))      # base64


# A3

import base64
from urllib.parse import unquote

def desfa(s):
    strat = ghici_strat(s)
    if strat == "base64":
        return strat, base64.b64decode(s)
    elif strat == "hex":
        return strat, bytes.fromhex(s)
    elif strat == "url":
        return strat, unquote(s).encode()
    return strat, s.encode()



#A4

def citibil(b):
    # True dacă toți octeții sunt caractere ASCII imprimabile (32..126)
    return all(32 <= c < 127 for c in b)

val = "NTM1OTU3NTk="
for i in range(8):
    strat, b = desfa(val)
    if citibil(b):
        print(f"Decodat cu succes la pasul {i+1} [{strat}]: {b.decode()}")
        break
    else:
        try:
            val = b.decode()
        except UnicodeDecodeError:
            print("Nu se mai poate decoda ca text.")
            break


#A5

date = open("probe/xor.bin", "rb").read()

for k in range(256):
    clar = bytes(b ^ k for b in date)
    if citibil(clar):
        print(f"Cheie XOR găsită: {k} (0x{k:02x}) -> Text: {clar.decode()}")


#A6

import hashlib

tinta = open("probe/hashuri.txt").readline().strip()
lungime = len(tinta)
print("Lungime hash:", lungime)   # 32 md5 / 40 sha1 / 64 sha256

for cuv in open("probe/wordlist.txt", encoding="latin1"):
    cuv = cuv.strip()
    cuv_bytes = cuv.encode()
    
    if lungime == 32:
        h = hashlib.md5(cuv_bytes).hexdigest()
    elif lungime == 40:
        h = hashlib.sha1(cuv_bytes).hexdigest()
    elif lungime == 64:
        h = hashlib.sha256(cuv_bytes).hexdigest()
    else:
        print("Algoritm necunoscut!")
        break

    if h == tinta:
        print("Parolă găsită:", cuv)
        break


#A7

import argparse
import base64
import hashlib
import json
import re
from urllib.parse import unquote

def ghici_strat(s):
    if "%" in s and re.search(r"%[0-9a-fA-F]{2}", s):
        return "url"
    if re.fullmatch(r"[0-9a-fA-F]+", s) and len(s) % 2 == 0:
        return "hex"
    if re.fullmatch(r"[A-Za-z0-9+/=]+", s) and len(s) % 4 == 0:
        return "base64"
    return "necunoscut"

def desfa(s):
    strat = ghici_strat(s)
    if strat == "base64":
        return strat, base64.b64decode(s)
    elif strat == "hex":
        return strat, bytes.fromhex(s)
    elif strat == "url":
        return strat, unquote(s).encode()
    return strat, s.encode()

def main():
    p = argparse.ArgumentParser(description="Decoder universal forensics")
    p.add_argument("intrare", help="Șir codat sau cale către fișier")
    p.add_argument("--fisier", action="store_true", help="Tratează intrarea ca fișier")
    a = p.parse_args()

    if a.fisier:
        date_raw = open(a.intrare, "rb").read()
        intrare_str = date_raw.decode(errors="ignore").strip()
    else:
        intrare_str = a.intrare

    strat, rez_bytes = desfa(intrare_str)
    
    fisa = {
        "strat": strat,
        "rezultat": rez_bytes.decode(errors="ignore")
    }

    with open("arsenal/forensics/fisa.json", "w", encoding="utf-8") as f:
        json.dump(fisa, f, indent=4)
        
    print(f"Decodat cu succes! Strat: {strat} | Salvat în arsenal/forensics/fisa.json")

if __name__ == "__main__":
    main()




