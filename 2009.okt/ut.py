class Auto:
    def __init__(self, ido, athaladas_mp, irany):
        self.ora = ido[0]
        self.perc = ido[1]
        self.mp = ido[2]
        self.athaladas_mp = athaladas_mp
        self.irany = irany
        self.erkezes_mp_ben = int(self.ora) * 3600 + int(self.perc) * 60 + int(self.mp)
        self.megerkezes_mp_ben = int(self.erkezes_mp_ben) + int(self.athaladas_mp)

    def get_mikor_hagyja_el(self):
        # perc = round(self.athaladas_mp / 60, 0)
        # mp = self.athaladas_mp % 60
        erkezes_mp_ben = self.megerkezes_mp_ben
        ora = int(list(str(erkezes_mp_ben / 3600).split("."))[0])
        erkezes_mp_ben -= ora * 3600
        perc = int(list(str(erkezes_mp_ben / 60).split("."))[0])
        erkezes_mp_ben -= perc * 60
        mp = erkezes_mp_ben

        return [f"{ora} ora {perc} perc {mp} masodperc", [ora, perc, mp]]

    def get_gyorsasag(self):
        meter_per_sec = round(1000/int(self.athaladas_mp), 1)
        return meter_per_sec

    def get_ora(self):
        return self.ora

    def get_irany(self):
        return self.irany

    def get_halad(self):
        if self.irany == "F":
            return "A"
        else:
            return "F"

    def get_erkezes_mp(self):
        return self.erkezes_mp_ben

    def get_megerkezes(self):
        return self.megerkezes_mp_ben

    def set_megerkezes(self, x):
        self.megerkezes_mp_ben = x

print("1. feladat adatok beolvasása")
autok = []
with open("forgalom.txt") as f:
    autok_szama = f.readline().rstrip()
    for line in f:
        sor = line.rstrip().split(" ")
        adat = Auto([sor[0], sor[1], sor[2]], sor[3], sor[4])
        autok.append(adat)

# 2.feladat
n_ertek = int(input("2. feladat: kérem adja meg a sorszámot: ")) - 1
auto = autok[n_ertek].get_halad()
if auto == "A":
    print("Az auto Alsó város felé halad")
else:
    print("Az auto a Felső város felé halad")

# 3.feladat
autok.reverse()
counter = 0
erkezes_egy = 0
erkezes_ketto = 0

for auto in autok:
    if auto.get_halad() == "F":
        counter += 1
        if counter == 1:
            erkezes_egy = auto.erkezes_mp_ben
            continue
        if counter == 2:
            erkezes_ketto = auto.erkezes_mp_ben
            break

print(f"3. feladat: Az utolsó két Felső város felé haladó autó {erkezes_egy - erkezes_ketto} mp különbséggel érte el a szakasz kezdetét")
autok.reverse()

f_orak = [[0] for x in range(0, 24)]
a_orak = [[0] for x in range(0, 24)]

for auto in autok:
    ora = auto.get_ora()
    irany = auto.get_irany()
    if irany == "F":
        f_orak[int(ora)].append("1")
    else:
        a_orak[int(ora)].append("1")
print("4. feladat:")
for index, x in enumerate(f_orak):
    if len(x) - 1 != 0 and len(a_orak[index]) - 1 != 0:
        print(f"{index} óra Alsó:{(len(a_orak[index]) - 1)} Felső:{len(x) - 1}")

# 5.feladat
autok_copy = autok
sebessegek = [x.get_gyorsasag() for x in autok]
sebessegek.sort(reverse=True)
sebessegek = sebessegek[:10]
print(sebessegek)
print("5.feladat:")
for x in sebessegek:
    counter = 0
    for index, y in enumerate(autok_copy):
        if x == y.get_gyorsasag():
            print(f"{y.ora}:{y.perc}:{y.mp} {y.get_irany()} {y.get_gyorsasag()}")
            counter += 1
            autok_copy.pop(index)
            if counter == 1:
                break

# 6.feladat
with open("also.txt", "w") as f:
    for index, auto in enumerate(autok):
        if index == 0:
            f.write(auto.get_mikor_hagyja_el()[0] + "\n")
        else:
            elozo = autok[index - 1].get_megerkezes()
            if elozo > auto.get_megerkezes():
                auto.set_megerkezes(elozo)
                f.write(auto.get_mikor_hagyja_el()[0] + "\n")





