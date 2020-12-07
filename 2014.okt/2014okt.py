#1. feladat
#foglaltsag beolvasasa
foglaltsag = []
with open("foglaltsag.txt") as f:
    for line in f:
        adat = line.strip()
        foglaltsag.append(list(adat))

kategoriak = []
with open("kategoria.txt") as f:
    for line in f:
        adat = line.strip()
        kategoriak.append(list(adat))

print(foglaltsag)
print(kategoriak)

print("2. feladat")
sor = input("kérlek adj meg egy sort: ")
oszlop = input("kérlek adj meg egy oszlopot: ")

hely = foglaltsag[int(sor) - 1][int(oszlop) - 1]
print(hely)
if hely == "x":
    print("a hely foglalt")
else:
    print("a hely szabad")
# 3.feladat
print("3. feladat")
eladottjegyek = 0
for lines in foglaltsag:
    eladottjegyek += lines.count("x")

print('Az előadásra eddig {0} jegyet adtak el, ez a nézőtér {1}%-a.'.format(eladottjegyek, round((eladottjegyek/300)*100)))
index = 0
egyes_kat = 0
kettes_kat = 0
harmas_kat = 0
negyes_kat = 0
otos_kat = 0
for lines in foglaltsag:
    helyertek = 0
    for hely in foglaltsag[index]:
        if hely == "x":
            kategora = kategoriak[index][helyertek]
            helyertek += 1
            if kategora == "1":
                egyes_kat += 1
            elif kategora == "2":
                kettes_kat += 1
            elif kategora == "3":
                harmas_kat += 1
            elif kategora == "4":
                negyes_kat += 1
            else:
                otos_kat += 1
        else:
            continue

    index += 1

sold = [egyes_kat, kettes_kat, harmas_kat, negyes_kat, otos_kat]
place = max(sold)
answer = sold.index(place) + 1
# 4. feladat
print("4. feladat")
print("A legtöbbet a {0} kategoriabol adtak el".format(answer))
print(egyes_kat, kettes_kat, harmas_kat, negyes_kat, otos_kat)

# 5. feladat
print("5. feladat")

bevetel = egyes_kat * 5000 + kettes_kat * 4000 + harmas_kat * 3000 + negyes_kat * 2000 + otos_kat * 1500
print("a jelenlegi bevétel: {0} lenne".format(bevetel))

# 6. feladat
print("6. feladat")

def szomszed_figy(sor, hely, foglalte):

    if hely == 0 or hely == 20:
        return 0

    else:
        if hely-1 == -1 or hely+1 > 20:
            return 0
        else:
            # 1
            # print(hely, sor)
            try:
                if foglalte[sor][hely-1] == "x" and foglalte[sor][hely+1] == "x":
                    return 1
                else:
                    return 0
            except Exception:
                print("out of index")
valasz = 0
index = 0
for line in foglaltsag:
    aktualis_hely = 0
    for hely in foglaltsag[index]:
        if hely == "o":
            if aktualis_hely == 20 or aktualis_hely == 0:
                pass
            else:
                print(aktualis_hely, index)
                ertek = (szomszed_figy(index, aktualis_hely, foglaltsag))
                if ertek is not None:
                    valasz += 1
                else:
                    pass
        else:
            pass
        aktualis_hely += 1
    index += 1

print("ennyi ilyen hely van: {0}".format(valasz))

# 7 feladat
print("7.feladat")

with open("szabad.txt", "w") as f:
    newlist = []
    for lineindex,line in enumerate(foglaltsag):
        append_string = ""
        for index, szek in enumerate(foglaltsag[lineindex]):
            if index == 19:
                if szek == "o":
                    add_that = kategoriak[lineindex][index]
                    append_string += add_that + "\n"
                else:
                    append_string += szek + "\n"
            else:
                if szek == "o":
                    add_that = kategoriak[lineindex][index]
                    append_string += add_that
                else:
                    append_string += szek
        newlist.append(append_string)

    for line in newlist:
        f.write(line)
