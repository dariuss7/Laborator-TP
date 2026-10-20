## Lucrarea A – Decoder universal

### Mesaj codificat în straturi

Mesajul a fost decodat treptat folosind tipurile de codare identificate de program.

Rezultat final:
SYWY

### XOR

Pentru fișierul xor.bin au fost încercate toate cele 256 de chei posibile.

Cheia XOR găsită: 128

Mesajul obținut:
Un singur octet tine tot secretul... gaseste-l! FLAG{xor_un_octet}

### Hash

Hash-ul analizat avea lungimea 32, deci algoritmul folosit era MD5.

Parola găsită: password


## Lucrarea B – Forensics pe fișiere

### Tipul real al fișierelor

Fișierul foto.jpg a fost identificat după magic bytes ca fiind JPEG.

Fișierul ascuns.png a fost identificat după semnătura sa reală ca fiind PNG.

### Metadate EXIF și GPS

Din fișierul foto.jpg au fost extrase metadatele EXIF.

Latitudine: 47.016666666666666
Longitudine: 28.8575

### File carving

În fișierul ascuns.png a fost găsită o arhivă ZIP lipită la sfârșitul imaginii.

Arhiva a fost extrasă în gasit.zip.

Conținutul arhivei:
FLAG{ascuns_prin_carving}

### Steganografie LSB

În imagine a fost ascuns un mesaj folosind ultimul bit al canalelor RGB.

Mesajul dezvăluit din stego.png:

FLAG{ascuns_in_pixeli}


## Challenge opțional

Fișierul challenge.bin conținea date codificate Base64, peste care era aplicat XOR.

După decodarea Base64 au fost încercate toate cele 256 de chei XOR.

Cheia găsită: 128

Mesajul obținut:

FLAG{lant_complet_despicat}