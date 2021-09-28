"""
Adott egy céltábla, amin egységnyi távolságra vannak a körök egymástól. Rálövünk a céltáblára, mennyit ér a lövés?
[0, 1]: 10 pont
[1, 2]: 9 pont
[2, 3]: 8 pont
…..
[9, 10]: 1 pont
[10, …]: 0 pont
"""

shot = int(input("Adjon le egy lövést: "))
pont = 10 - shot
print(f"Az ön pontszáma: {pont}")
