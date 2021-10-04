# HF: két pozitív egész szám relatív prím-e

# két szám akkor relatív prímek ha legnagyobb közös
# osztólyuk az 1

a = int(input("Adja meg az első számot: "))
b = int(input("Adja meg az második számot: "))

while b != 0:
    r = a % b
    a = b
    b = r

if a == 1:
    print("A két szám egymás relatív prímjei.")
else:
    print("A két szám nem relatív prím.")