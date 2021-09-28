# 2 síkbeli egyenes metszéspontjának meghatározása!

a1 = int(input("Adja meg az e egyenes a1 együtthatóját: "))
b1 = int(input("Adja meg az e egyenes b1 együtthatóját: "))
c1 = int(input("Adja meg az e egyenes c1 együtthatóját: "))

a2 = int(input("Adja meg az f egyenes a2 együtthatóját: "))
b2 = int(input("Adja meg az f egyenes b2 együtthatóját: "))
c2 = int(input("Adja meg az f egyenes c2 együtthatóját: "))

x1 = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
y1 = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)

print(f"A két egyenes metszéspontja: ({x1}, {y1})")
