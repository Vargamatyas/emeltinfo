class Pont:
    def __init__(self, szin):
        self.szin = szin

    def get_szin(self):
        return self.szin

    def set_szin(self, uj_szint):
        self.szin = uj_szint


class Kep:
    def __init__(self):
        self.sorok = []

    def add_sor(self, sor):
        self.sorok.append(sor)

    def get_sor(self,hely):
        return [x.get_szin() for x in self.sorok[hely]]

    def get_pont(self, sor, oszlop):
        return self.sorok[sor][oszlop].get_szin()

    def get_oszlop(self, oszlop):
        oszlop_tartalma = []

        for elem in self.sorok:
            uj_elem = elem[oszlop].get_szin()
            oszlop_tartalma.append(uj_elem)

        return oszlop_tartalma

    def atszinezni_sort(self, sorszam, szin):
        for x in self.sorok[sorszam]:
            x.set_szin(szin)

    def atszinezes_oszlop(self, oszlopszam, szin):

        for x in self.sorok:
            x[oszlopszam].set_szin(szin)

    def get_sorok(self):
        return self.sorok

sorok = []
with open('kep.txt') as f:
    for line in f:
        sorok.append(line.rstrip())

szinek_halmaza = set(sorok)

kep = Kep()
ideiglenes_sor = []
counter = 0
for line in sorok:
    if counter == 50:
        kep.add_sor(ideiglenes_sor)
        ideiglenes_sor = []
        counter = 0
    ideiglenes_pont = Pont(line)
    ideiglenes_sor.append(ideiglenes_pont)
    counter += 1


# 2.feladat
szin = input('Kérem adjon meg egy RGB kódot: ')
valasz = False
if szin in szinek_halmaza:
    valasz = True
    print('A szín megtalálható a képen!')
else:
    print('A szín nem található meg a képen')

# 3.feladat

pont_szin = kep.get_pont(34, 7)
sor = kep.get_sor(34)
sorban = sor.count(pont_szin)
oszlop = kep.get_oszlop(7)
oszlopban = oszlop.count(pont_szin)
print(f'Sorban: {sorban}, Oszlop: {oszlopban}')

# 4.feladat

kek = sorok.count("0 0 255")
voros = sorok.count("255 0 0")
zold = sorok.count("0 255 0")

legtobbszor = 0
if kek > voros and zold:
    legtobbszor = kek
    print("4.feladat: Kék")
else:

        if voros > kek and zold:
            legtobbszor = voros
            print("4.feladat: Vrös")
        else:
            legtobbszor = zold
            print("4.feladat: Zöld")

# 5.feladat

kep.atszinezni_sort(0, "0 0 0")
kep.atszinezni_sort(1, "0 0 0")
kep.atszinezni_sort(2, "0 0 0")
kep.atszinezni_sort(46, "0 0 0")
kep.atszinezni_sort(47, "0 0 0")
kep.atszinezni_sort(48, "0 0 0")
kep.atszinezes_oszlop(0, "0 0 0")
kep.atszinezes_oszlop(1, "0 0 0")
kep.atszinezes_oszlop(2, "0 0 0")
kep.atszinezes_oszlop(47, "0 0 0")
kep.atszinezes_oszlop(48, "0 0 0")
kep.atszinezes_oszlop(49, "0 0 0")

# 6.feladat
kirashoz_sorok = kep.get_sorok()
with open("keretes.txt", "w") as f:
    for x in kirashoz_sorok:
        for y in x:
            f.write(y.get_szin() + "\n")

# 7.feladat
kezdet_sor = " "
kezdet_oszlop = " "
found = False
for index, x in enumerate(sorok):
    if x == "255 255 0":
        kezdet_sor = round((index/50))
        if index < 50:
            kezdet_sor = 0
        kezdet_oszlop = index - (kezdet_sor*50)

sumsorok = len(sorok)
vege_sor = " "
vege_oszlop = ""
sorok.reverse()
for index, x in enumerate(sorok):
    if x == "255 255 0":
        vege_sor = 50 - (round((index/50))+1)
        if index < 50:
            kezdet_sor = 0
        vege_oszlop = sumsorok - (vege_sor*50)

szinek = []
for x in kirashoz_sorok:
    for y in x:
        szinek.append(y.get_szin())

db = szinek.count("255 255 0")
print(f"Kezd: {kezdet_sor + 1}, {kezdet_oszlop + 1} \nVége: {vege_sor}, {vege_oszlop}\nKéppontok száma: {db}")

