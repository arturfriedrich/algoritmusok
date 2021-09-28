# HF: Hogyan lehet eldönteni egy számról, hogy prímszám-e
import math

number = int(input("Adjon meg egy számot: "))

if number > 1:
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            print(number, "nem prímszám.")
            break
    else:
        print(number, "egy prímszám.")
else:
    print(number, "egy prímszám.")
