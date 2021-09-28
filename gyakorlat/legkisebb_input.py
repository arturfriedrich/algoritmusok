# 3 input szám esetén írja ki a legkisebb értékét!

num1 = int(input("Adjon megy egy számot: "))
num2 = int(input("Adjon megy egy számot: "))
num3 = int(input("Adjon megy egy számot: "))

minimum = num1

if num1 < num2:
    minimum = num1
elif num2 < num3:
    minimum = num2
elif num3 < minimum:
    minimum = num3

print(f"A legkisebb érték a megadott számok közül a {minimum}")
