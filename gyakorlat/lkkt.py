# két pozitív egész szám legkisebb közös többszöröse!

a = int(input("Az első szám: "))
b = int(input("A második szám: "))

if a > b:
    a, b = b, a

lkkt = b
while lkkt % a != 0:
    lkkt += b


print("A legkisebb közös többszörös:", lkkt)


