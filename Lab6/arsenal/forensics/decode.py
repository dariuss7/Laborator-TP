# A1
s = "Salut"
b = s.encode()          # bytes
print(b, b[0])          # b"Salut" 83
print(b.hex())
hex_text = b.hex()
refacut = bytes.fromhex(hex_text)
print(refacut)



# A2
import re
def ghici_strat(s):
    if re.search(r"%[0-9A-Fa-f]{2}", s):
        return "url"
    if len(s) % 2 == 0 and re.fullmatch(r"[0-9A-Fa-f]+", s):
        return "hex"
    if re.fullmatch(r"[A-Za-z0-9+/=]+", s):
        return "base64"

    return "necunoscut"
print(ghici_strat("%2Fetc"))   # url
print(ghici_strat("48656c6c6f"))  # hex



# A3
import base64
from urllib.parse import unquote
def desfa(s):
    strat = ghici_strat(s)
    if strat == "base64":
        rezultat = base64.b64decode(s)
    elif strat == "hex":
        rezultat = bytes.fromhex(s)
    elif strat == "url":
        rezultat = unquote(s).encode()
    else:
        rezultat = s.encode()
    return strat, s.encode()



# A4
val = "NTM1OTU3NTk="

for _ in range(8):
    strat, b = desfa(val)

    print(strat, b)

    text = b.decode()

    if strat == "hex" and citibil(b):
        print(text)
        break

    val = text


# A5
date = open("probe/xor.bin", "rb").read()
for k in range(256):
    clar = bytes(b ^ k for b in date)
    if citibil(clar):
        print("cheie:", k, clar.decode())



# A6
import hashlib
tinta = open("probe/hashuri.txt").readline().strip()
print(len(tinta))   # 32 md5 / 40 sha1 / 64 sha256
for cuv in open("probe/wordlist.txt", encoding="latin1"):
    cuv = cuv.strip()
    if len(tinta) == 32:
        hash_cuv = hashlib.md5(cuv.encode()).hexdigest()

    elif len(tinta) == 40:
        hash_cuv = hashlib.sha1(cuv.encode()).hexdigest()

    elif len(tinta) == 64:
        hash_cuv = hashlib.sha256(cuv.encode()).hexdigest()

    if hash_cuv == tinta:
        print("gasit:", cuv)
        break



# A7
import argparse, json
import argparse, json
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("intrare", nargs="?")   # sir sau cale
    p.add_argument("--fisier", action="store_true")
    a = p.parse_args()
    if a.intrare is not None:
        if a.fisier:
            intrare = open(a.intrare, "rb").read().decode()
        else:
            intrare = a.intrare
        strat, b = desfa(intrare)
        with open("arsenal/forensics/fisa.json", "w") as file:
            json.dump({
                "strat": strat,
                "rezultat": b.decode()
            }, file, indent=2)
        print("Strat:", strat)
        print("Rezultat:", b.decode())


# B1
def tip_real(cale):
    cap = open(cale, "rb").read(8)
    if cap.startswith(b"%PDF"):
        return "pdf"
    if cap.startswith(b"\x89PNG"):
        return "png"
    if cap.startswith(b"\xff\xd8"):
        return "jpeg"
    if cap.startswith(b"PK\x03\x04"):
        return "zip/docx"
    return cap.hex()
print(tip_real("probe/foto.jpg"))

# B2
import re
date = open("probe/ascuns.png", "rb").read()
for m in re.findall(rb"[ -~]{4,}", date):
    print(m.decode())
# B3
from PIL import Image
exif = Image.open("probe/foto.jpg")._getexif() or {}
gps = exif.get(34853)
if gps:
    lat = gps[2]
    lon = gps[4]
    latitudine = float(lat[0]) + float(lat[1]) / 60 + float(lat[2]) / 3600
    longitudine = float(lon[0]) + float(lon[1]) / 60 + float(lon[2]) / 3600
    if gps[1] == "S":
        latitudine = -latitudine
    if gps[3] == "W":
        longitudine = -longitudine
    print("Latitudine:", latitudine)
    print("Longitudine:", longitudine)


# B4
date = open("probe/ascuns.png", "rb").read()
i = date.find(b"PK\x03\x04")
if i != -1:
    open("gasit.zip", "wb").write(date[i:])
    print("arhiva extrasa de la octetul", i)


# B5
from PIL import Image
img = Image.open("probe/foto.jpg").convert("RGB")
px = list(img.getdata())
mesaj = b"FLAG{ascuns_in_pixeli}\x00"
biti = "".join(f"{x:08b}" for x in mesaj)
px_nou = []
i = 0
for pixel in px:
    pixel = list(pixel)
    for canal in range(3):
        if i < len(biti):
            pixel[canal] = (pixel[canal] & ~1) | int(biti[i])
            i += 1
    px_nou.append(tuple(pixel))
img.putdata(px_nou)
img.save("stego.png")

# B6
px = list(Image.open("stego.png").convert("RGB").get_flattened_data())
biti = ""
for (r, g, b) in px:
    biti += str(r & 1)
    biti += str(g & 1)
    biti += str(b & 1)
mesaj = b""
for i in range(0, len(biti), 8):
    octet = int(biti[i:i+8], 2)
    if octet == 0:
        break
    mesaj += bytes([octet])
print(mesaj.decode())


# Pentru varful salii
import base64
date = open("probe/challenge.bin", "rb").read().strip()
date = base64.b64decode(date)
for k in range(256):
    clar = bytes(b ^ k for b in date)
    if b"FLAG{" in clar:
        print("cheie:", k)
        print("mesaj:", clar.decode())