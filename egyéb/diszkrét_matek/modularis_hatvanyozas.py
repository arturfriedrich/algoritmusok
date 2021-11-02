from math import *

# adatbekérés
alap = int(input("Adja meg az alapot: "))
alap_hatvany = int(input("Adja meg az alap hatványát: "))
alap_oszto = int(input("Adja meg az osztót: "))
hatvany = alap_hatvany

results = list()
results.append(alap)

# moduláris hatványozás elvégzése
for i in range(10):
    res = pow(results[i], 2) % alap_oszto
    results.append(res)

# kettő hatványai
powers = [1, 2]
power = 2
while power < alap_hatvany - power:
    powers.append(power * 2)
    power *= 2

z = list()

powers = list(reversed(powers))
for i in range(len(powers)):
    if alap_hatvany - powers[i] >= 0:
        alap_hatvany = alap_hatvany - powers[i]
        z.append(i)

for i in range(len(z)):
    z[i] = max(z) - z[i]

összeg = 1
for i in range(len(z)):
    összeg *= results[z[i]]

end = összeg % alap_oszto
print(f"A(z) {alap} a(z) {hatvany}. hatványon-nak vett maradéka {alap_oszto}-el:", end)