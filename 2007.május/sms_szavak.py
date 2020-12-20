# 1 feladat
print("1. feladat")
betu_szam_dict = {"A": "2", "B": "2", "C": "2", "D": "3", "E": "3", "F": "3", "G": "4", "H": "4", "I": "4",
                  "J": "5", "K": "5", "L": "5", "M": "6", "N": "6", "O": "6"
                    ,"P": "7", "Q": "7", "R": "7", "S": "7", "T": "8", "U": "8", "V": "8", "W": "9",
                  "X": "9", "Y": "9", "Z": "9"}

betu = input("Kérem adjon meg egy betűt!")
print(betu_szam_dict.get(betu.upper()))

# 2. feladat
print("2. feladat")
szo = input("kérem adjon meg egy szót!")
szamsor = ""

for i in szo:
    szamsor += betu_szam_dict.get(i.upper())

print("A szót ezzel a számsorral lehet bevinni: {0}".format(szamsor))

# 3.feladat
print("3. feladat")

lines = []
with open("szavak.txt") as f:
    for line in f:
        lines.append(line.rstrip())

aktualis_leghosszabb_szo = ""
hossza = 0

#4. feladat
print("4.feladat")
for line in lines:
    akt_hossz = len(line)
    if akt_hossz > hossza:
        hossza = len(line)
        aktualis_leghosszabb_szo = line

print("A leghosszab szó: {0}, hossza: {1}".format(aktualis_leghosszabb_szo, hossza))

#5. feladat
print("5. feladat")

rovid_szavak = 0
for szo in lines:
    hossz = len(szo)
    if hossz <= 5:
        rovid_szavak += 1
    else:
        pass

print("{0}-rövid szó van a fájlban".format(rovid_szavak))

# 6.feladat
print("6.feladat")
kodok = []
with open("kodok.txt", "w") as f:
    for szavacska in lines:
        aktualis_szamkod = ""
        for betu in szavacska:
            aktualis_szamkod += betu_szam_dict.get(betu.upper())
        f.write(aktualis_szamkod + "\n")
        kodok.append(aktualis_szamkod)

# 7.feladat
print("7. feladat")
aktualis_szamkod = input("kérem adjon meg egy számsort!")

valaszok = []


for i in lines:
    valasz = ""
    for character in i:
        valasz += betu_szam_dict.get(character.upper())
    if valasz == aktualis_szamkod:
        valaszok.append(i)

print("A számsorhoz, ezek a szavak tartozhatnak:{0}".format(" ,".join(valaszok)))

#8. feladat
print("8. feladat")
legtobb_ismetlodo = 0
annak_kodja = ""
annak_szava = []
nyolcas_vegleges = []
szamok = []
for i in list(set(kodok)):
    nyolcas_valaszok = []
    for y in lines:
        szamsor = ""
        for betu in y:
            szamsor += betu_szam_dict.get(betu.upper())
        if szamsor == i:
            print([szamsor, i, y])
            nyolcas_valaszok.append(y)
        else:
            continue
    print(nyolcas_valaszok)
    if len(nyolcas_valaszok) >= 2:
        for x in nyolcas_valaszok:
            valasz_string = "{0} : {1}".format(x, i)
            nyolcas_vegleges.append(valasz_string)

        if len(nyolcas_valaszok) > legtobb_ismetlodo:
            annak_szava = []
            legtobb_ismetlodo = len(nyolcas_valaszok)
            annak_kodja = i
            for szo in nyolcas_valaszok:
                annak_szava.append(szo)
        else:
            continue
    else:
        continue
print(",".join(nyolcas_vegleges))

# 9. feladat
print("9. feladat")
szavak_listaja = " ,".join(annak_szava)
print("A legtöbbször ismétlődő kód a {0}, ennek szavai: {1}".format(annak_kodja, szavak_listaja))
