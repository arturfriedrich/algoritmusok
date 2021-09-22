sz = int(input("sz: "))
m = int(input("m: "))
h = int(input("h: "))
ajm = int(input("ajm: "))
ajsz = int(input("ajsz: "))
abm = int(input("abm: "))
absz = int(input("absz: "))
fk = int(input("fk: "))

ajt = ajm * ajsz
abt = abm * absz
szf = (2 * (sz*m + h*m)) - (ajt + abt)
er = szf / fk
print("A szoba kifestéséhez", er, "liter festék kell")

