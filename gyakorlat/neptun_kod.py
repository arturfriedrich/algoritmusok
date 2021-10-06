import random

neptunkod = ""

for i in range(6):
    neptunkod += chr(random.randint(65, 90))

print(neptunkod)

lk = ""
for i in range(10):
    lk += str(i)
for i in range(65, 90):
    lk += chr(i)

ne = ""
for i in range(6):
    ne += str(random.choice(lk))

print(ne)


