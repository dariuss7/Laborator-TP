#B1

def tip_real(cale):
    cap = open(cale, "rb").read(8)
    if cap.startswith(b"%PDF"):
        return "pdf"
    elif cap.startswith(b"\x89PNG"):
        return "png"
    elif cap.startswith(b"\xff\xd8"):
        return "jpeg"
    elif cap.startswith(b"PK\x03\x04"):
        return "zip/docx"
    return cap.hex()

print("Tipul real foto.jpg:", tip_real("probe/foto.jpg"))


#B2

import re

date = open("probe/ascuns.png", "rb").read()
print("Secvențe ASCII găsite în ascuns.png:")
for m in re.findall(rb"[ -~]{4,}", date):
    print(m.decode())


#B3

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

img = Image.open("probe/foto.jpg")
exif = img._getexif() or {}

for id_tag, val in exif.items():
    nume_tag = TAGS.get(id_tag, id_tag)
    print(f"{nume_tag} = {val}")

# Extragere GPS (tag 34853)
gps_info = exif.get(34853)
if gps_info:
    print("\n--- Informații GPS ---")
    gps_data = {}
    for t in gps_info:
        sub_tag = GPSTAGS.get(t, t)
        gps_data[sub_tag] = gps_info[t]
    
    print("Latitudine:", gps_data.get("GPSLatitude"), gps_data.get("GPSLatitudeRef"))
    print("Longitudine:", gps_data.get("GPSLongitude"), gps_data.get("GPSLongitudeRef"))




#B4

import zipfile

date = open("probe/ascuns.png", "rb").read()
i = date.find(b"PK\x03\x04")

if i != -1:
    open("gasit.zip", "wb").write(date[i:])
    print(f"Arhivă extrasă de la octetul {i} și salvată în gasit.zip")
    
    # Dezarhivare automată
    with zipfile.ZipFile("gasit.zip", "r") as zip_ref:
        zip_ref.extractall("extrase/")
    print("Conținut dezarhivat în folderul extrase/")


#B5

from PIL import Image

img = Image.open("probe/foto.jpg").convert("RGB")
px = list(img.getdata())

# Adăugăm octetul 0x00 (\x00) la final pentru a semnaliza sfârșitul mesajului
mesaj = b"FLAG{ascuns_in_pixeli}\x00"
biti = "".join(f"{x:08b}" for x in mesaj)

px_nou = []
bit_idx = 0
num_bits = len(biti)

for r, g, b in px:
    canale = [r, g, b]
    for c_idx in range(3):
        if bit_idx < num_bits:
            canale[c_idx] = (canale[c_idx] & ~1) | int(biti[bit_idx])
            bit_idx += 1
    px_nou.append(tuple(canale))

img_stego = Image.new(img.mode, img.size)
img_stego.putdata(px_nou)
img_stego.save("stego.png")
print("Mesaj ascuns cu succes în stego.png")


#B6

from PIL import Image

img_stego = Image.open("stego.png").convert("RGB")
px = list(img_stego.getdata())

biti = ""
for r, g, b in px:
    biti += str(r & 1)
    biti += str(g & 1)
    biti += str(b & 1)

octeti = bytearray()
for i in range(0, len(biti), 8):
    bloc = biti[i:i+8]
    if len(bloc) < 8:
        break
    val_octet = int(bloc, 2)
    if val_octet == 0:  # Delimitatorul de final de mesaj (\x00)
        break
    octeti.append(val_octet)

print("Mesaj dezvăluit din LSB:", octeti.decode(errors="ignore"))

