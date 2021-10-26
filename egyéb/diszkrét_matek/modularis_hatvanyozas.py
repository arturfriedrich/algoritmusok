from math import *

print(pow(2, 6))
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

sum = 1
for i in range(len(z)):
    print(results[z[i]])
    sum *= results[z[i]]

end = sum % alap_oszto
print("End:", end)