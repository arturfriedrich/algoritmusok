from math import *

# alap = int(input("Adja meg az alapot: "))
# alap_hatvany = int(input("Adja meg az alap hatványát: "))
# alap_oszto = int(input("Adja meg az osztót: "))

alap = 52
alap_hatvany = 79
alap_oszto = 253

results = list()
results.append(alap)

# moduláris hatványozás elvégzése
for i in range(10):
    res = pow(results[i], 2) % alap_oszto
    results.append(res)

# kettő hatványainak megtalálása
powers = [2]
power = 2
while power < alap_hatvany:
    powers.append(power * 2)
    power *= 2
print(powers)

print(results)