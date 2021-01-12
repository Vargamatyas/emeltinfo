# 1.feladat
print("1. feladat")
bekert_szo = input("Adjon meg egy szót: ")
maganhangzok = ["a", "e", "i", "o", "u"]

cond = False
for c in maganhangzok:
    if c in bekert_szo:
        cond = True
        break
    else:
        continue

if cond is True:
    print("Van benne magánhangzó.")

else:
    print("Nincs benne magánhangzó.")

# 2.feladat
print("2. feladat")

szavak = []
with open("szoveg.txt") as f:
    for line in f:
        sor = line.rstrip()
        szavak.append(sor)

leghosszabb_szo = ""
eddigi_int = 0
for szo in szavak:
    hossz = len(szo)
    if hossz > eddigi_int:
        eddigi_int = hossz
        leghosszabb_szo = szo
    else:
        continue

print(f"A leghosszabb szó: {leghosszabb_szo}, {len(leghosszabb_szo)} db karakter hosszúságú.")

# 3. feladat
print("3.feladat")


def maganhangzo_kereso(szoo):
    maganhangzok = ["a", "e", "i", "o", "u"]
    szo_hossz = len(szoo)
    maganhangzok_szama = 0

    for i in szoo:
        if i in maganhangzok:
            maganhangzok_szama += 1
        else:
            pass

    returnable = False
    if maganhangzok_szama > szo_hossz / 2:
        returnable = True

    else:
        pass

    return returnable


szavak_szama = len(szavak)
tobb_a_maganhangzo = []
counter = 0
for szo in szavak:
    cond = maganhangzo_kereso(szo)
    if cond is True:
        tobb_a_maganhangzo.append(szo)
        counter += 1
    else:
        pass

print(" ".join(tobb_a_maganhangzo))
print(f"{counter}/{szavak_szama} : {round((counter/szavak_szama)*100, 2)}%")

# 4.feladat
print("4.feladat")

otkarakteres = []

for szo in szavak:
    lenght = len(szo)
    if lenght == 5:
        otkarakteres.append(szo)
    else:
        continue

szoreszlet = input("Kérem adjon meg egy szórészletet: ")
megoldasok = []
for i in otkarakteres:
    szo_kozepe = i[1:4]
    if szo_kozepe == szoreszlet:
        megoldasok.append(i)
    else:
        continue

print(megoldasok)

# 5.feladat
print('5. feladat')

with open("letra.txt", "a+") as f:
    lenght = len(f.read())

    for index, i in enumerate(megoldasok):
        if index == 0 and lenght == 0:
            f.write(i + "\n")
            continue
        else:
            f.write(i + "\n")
    f.write("\n")

