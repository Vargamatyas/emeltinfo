with open("lottosz.dat") as f:
    sorok = []
    for line in f:
        sor = (line.rstrip().split(" "))
        sor.sort(reverse=True)
        sorok.append(sor)

# 1. feladat
bekert_sor = (input("Kérem adja meg az 52.heti lottószámokat: ").split(" "))
bekert_sor.sort(reverse=True)
print(" ".join(bekert_sor))

# 3.feladat
szam = input("Kérem adjon meg egy számot 1 - 51 között: ")
print(" ".join(sorok[int(szam) - 1]))
# 4 feladat
szamok = [str(x) for x in range(1, 91)]

van_olyan_szam = False
for szam in szamok:
    aktualis_sor = False
    for sor in sorok:
        if szam in sorok:
            aktualis_sor = True

    if aktualis_sor is False:
        van_olyan_szam = True

if van_olyan_szam is True:
    print("Igen van olyan szám amit nem húztak ki.")

# 6. feladat
counter = 0
for sor in sorok:
    for element in sor:
        if int(element) % 2 == 0:
            counter += 1

paratlanok = (51 * 5) - counter
print(f"{paratlanok}-szor húztak páratlan számot.")

sorok.append(bekert_sor)
# 7. feladat
with open("lotto52.txt", "w") as f:
    for sor in sorok:
        f.write(" ".join(sor) + "\n")

printable_sor = []
final_printable = []
for szam in szamok:
    szam_counter = 0
    for sor in sorok:
        if szam in sor:
            szam_counter += 1

    printable_sor.append(szam_counter)
    if len(printable_sor) % 15 == 0:
        final_printable.append(str(printable_sor))
        printable_sor = []

for x in final_printable:
    print_this = " ".join(x)
    print(print_this)

prim_szamok = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
prim_szamok = [str(x) for x in prim_szamok]
megoldasok = []
for prim in prim_szamok:
    primszam_status = False
    for sor in sorok:
        if prim in sor:
            primszam_status = True
        else:
            continue

    if primszam_status is True:
        continue
    else:
        megoldasok.append(str(prim))

if len(megoldasok) == 0:
    print("Minden prímszámot kihúztak 100-ig")
else:
    megoldas = ", ".join(megoldasok)
    print(f"Ezeket a prímszámokat ben húzták ki az évben: {megoldas}")



