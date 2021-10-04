# Adott N darab input adat, mondjuk meg, hogy a megadott számok közül pozitívból vagy
# negatívból volt-e több, illetve azt, hogy mennyivel.

n = int(input("Adja meg az adatok darabszámát: "))
counter = 0
i = 1
for i in range(0, n):
    a = int(input("Adjon meg egy számot: "))
    if a > 0:
        counter += 1
    elif a < 0:
        counter -= 1

if counter > 0:
    print(f"Pozitív számból van több, {counter} darabbal.")
elif counter < 0:
    print(f"Negatív számból van több, {counter} darabbal.")
else:
    print("Ugyan annyi van belőlük.")