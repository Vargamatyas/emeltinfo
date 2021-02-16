# 2. feladat beolvasás
szavak = []
with open("szotar.txt") as f:
    for line in f:
        sor = line.rstrip()
        szavak.append(sor)

# 1.feladat
szo = input("1. feladat kérem adjon meg egy szavat: ")
kulonbozo = list(set(list(szo)))
print(f"A szóban {len(kulonbozo)} db kulonbozo karakter van ezek pedig a: {' ,'.join(kulonbozo)}" )

# 3. feladat
abcrendben = []
for x in szavak:
    szo = list(x)
    szo.sort()
    uj_str = "".join(szo)
    abcrendben.append(uj_str)

elso_szo = input("4. feladat, kérem adjon meg egy szót: ")
masodik_szo = input("kérem adja meg a második szavat: ")


def anagramma(elso, masodik):
    elso_szo = list(set(list(elso)))
    maso_szo = list(set(list(masodik)))
    if len(elso) == len(masodik):
        if elso_szo.sort() == maso_szo.sort():
            cond = True
            for x in elso_szo:
                ertek_egy = list(elso).count(x)
                ertek_ketto = list(masodik).count(x)

                if ertek_egy == ertek_ketto:
                    continue
                else:
                    cond = False
                    break
            if cond is True:
                return True
            else:
                return False

        else:
            return False
    else:
        return False


returnable = anagramma(elso_szo, masodik_szo)
if returnable is True:
    print("Anagramma")
else:
    print("Nem anagramma")

keresett_szo = input("6. feladat: Kérem adja meg a keresett szavat: ")
megoldasok = []
for x in szavak:
    if anagramma(keresett_szo, x) is True:
        megoldasok.append(x)
        continue
    else:
        pass

if len(megoldasok) == 0:
    print("Nincs a szótárban anagramma")
else:
    print(" ".join(megoldasok))

# 6. feladat
current_szo = " "
current_lenght = 0
for y in szavak:
    hossza = len(y)
    if hossza > current_lenght:
        current_lenght = hossza
        current_szo = y

anagramma_jeloltek = []
for x in szavak:
    if len(x) == current_lenght:
        anagramma_jeloltek.append(x)

final_list = []
for index, x in enumerate(anagramma_jeloltek):
    aktualis_list = []
    for y in anagramma_jeloltek[:index]:
        if anagramma(x, y) is True:
            aktualis_list.append(y)

    if len(final_list) < len(aktualis_list):
        aktualis_list.append(x)
        final_list = aktualis_list

for x in final_list:
    print(x)

szavak.sort(key=len)

with open("rendezve.txt", "w") as f:
    previous = len(szavak[0])
    for index, x in enumerate(szavak):
        temp_list = [x]
        hossz = len(x)
        szavak.pop(index)
        if hossz > previous:
            f.write("\n")
            previous = hossz
        for y in szavak:
            if anagramma(x, y) is True:
                temp_list.append(y)
                index = szavak.index(y)
                szavak.pop(index)
                continue
        f.write(" ".join(temp_list) + "\n")
