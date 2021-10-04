# HF: adott a és b zárt intervallumba eső
#             - prímek kiirása
#             - relatív prímpárok kiírása

a = int(input("Adja meg az intervallum elejét: "))
b = int(input("Adja meg az intervallum végét: "))
primes = list()
relatively_primes = list()

for number in range(a, b):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                break
        else:
            primes.append(number)
    else:
        primes.append(number)
print(primes)

for x, y in range(a, b):
    while y != 0:
        r = x % y
        x = y
        y = r
        if x == 1:
            print(x, y)

if a == 1:
    print("A két szám egymás relatív prímjei.")
else:
    print("A két szám nem relatív prím.")
