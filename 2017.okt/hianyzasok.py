class Nap:

    def __init__(self, datum):
        self.datum = datum
        self.hianyzok = {}
        self.igazolt_h = 0
        self.igazolatlan = 0
        self.nincs_ora = 0
        self.datum_torve = datum.split(" ")
        self.nap = self.hetnapja(int(self.datum_torve[0]), int(self.datum_torve[1]))
        self.orak = []

    def add_to_hianyzok(self, nev, hianyzo_sor):
        self.hianyzok[nev] = hianyzo_sor

        for char in hianyzo_sor:
            self.orak.append(char)
            if char == "X":
                self.igazolt_h += 1
                continue
            if char == "I":
                self.igazolatlan += 1
                continue
            if char == "N":
                self.nincs_ora += 1
                continue

    def get_ora(self, ora):
        return self.orak[int(ora) - 1]

    def get_igazolt_es_igazolatlan(self):
        return [self.igazolt_h, self.igazolatlan]

    def hetnapja(self, honap, nap):
        napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok",
                  "pentek", "szombat"]

        napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]

        napsorszam = (napszam[honap - 1] + nap) % 7

        return napnev[napsorszam]

    def get_nap(self):
        return self.nap

# 1.feladat beolvasás

sorok_szama = []
with open("naplo.txt") as f:
    for line in f:
        sor = line.rstrip()

        if "#" not in sor:
            sorok_szama.append(sor)
        else:
            continue

# 2.feladat
print(f"A fájlban {len(sorok_szama)} db olyan sor van ami hiíányzást rögzít.")

#3. feladat
sorok = []
with open("naplo.txt") as f:
    for line in f:
        sorok.append(line.rstrip())

aktualis_nap = " "
napok = []
sorok_szama = len(sorok)

for index, line in enumerate(sorok):
    if index + 1 == sorok_szama:
        napok.append(aktualis_nap)

    if "#" in line:
        napok.append(aktualis_nap)
        line_data = line.split(" ")
        nap = Nap(line_data[1] + " " + line_data[2])
        aktualis_nap = nap

    else:
        gyerek_adat = line.split()
        nev = gyerek_adat[0] + " " + gyerek_adat[1]
        hianyzas_sor = gyerek_adat[2]
        aktualis_nap.add_to_hianyzok(nev, hianyzas_sor)

napok.pop(0)

igazolt_hianyzasok = 0
igazolatlan_hianyzasok = 0

for i in napok:
    adat = i.get_igazolt_es_igazolatlan()
    igazolt = adat[0]

    igazolt_hianyzasok += igazolt
    igazolatlan = adat[1]
    igazolatlan_hianyzasok += igazolatlan

print(f"3. feladat: {igazolt_hianyzasok} db igazolt és {igazolatlan_hianyzasok} db igazolatlan hiányzás volt a félév során")


def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok",
                "pentek", "szombat"]

    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]

    napsorszam = (napszam[honap-1] + nap) % 7
    return (napnev[round(napsorszam)])

# 5.feladat
datum = input("Kérem adjon meg egy dátumot:(kérem szóközzel szeparálja): ").split(" ")
nap = hetnapja(int(datum[0]), int(datum[1]))
print(f"5. feladat: A nap {nap}.")


# 6.feladat
valasztott_nap = input("kérem adja meg a választott napot és az órát(szóközzel elválasztva): ").split(" ")

szamlalo = 0
for i in napok:
    nap = i.get_nap()

    if nap == valasztott_nap[0]:
        ora_allapota = i.get_ora(valasztott_nap[1])
        if ora_allapota == "X" or "I":
           szamlalo += 1
    else:
        continue

print("6.feladat: A napra {0} hiányzás jutott a félévben.".format(str(szamlalo)))

# 7. feladat


class Tanulo:
    def __init__(self, nev):
        self.hianyzas = 0
        self.nev = nev

    def add_hianyzas(self, string):
        for i in string:
            if i == "X" or "I":
                self.hianyzas += 1

    def get_hianyzas(self):
        return self.hianyzas

    def return_name(self):
        return nev


tanulok_hianyzasai = []

with open("naplo.txt") as f:
    for line in f:
        sor = line.rstrip()
        if "#" not in sor:
            tanulok_hianyzasai.append(sor)


tanulok_listaja = []
tanulok_obj = []
for i in tanulok_hianyzasai:
    y = i.split(" ")
    neve = y[0] + " " + y[1]
    if neve not in tanulok_listaja:

        tanulok_listaja.append(neve)
        uj_tanulo = Tanulo(neve)
        uj_tanulo.add_hianyzas(y[2])
        tanulok_obj.append(uj_tanulo)
    else:
        index = tanulok_listaja.index(neve)
        aktualis_obj = tanulok_obj[index]
        aktualis_obj.add_hianyzas(y[2])

legmagasabb = 0
nyertes = []
print(tanulok_listaja)
for x in tanulok_obj:
    aktualis_hianyzas = x.get_hianyzas()
    if aktualis_hianyzas > legmagasabb:
        nyertes = []
        legmagasabb = aktualis_hianyzas
        nev = x.return_name()
        nyertes.append(nev)
        continue

    if aktualis_hianyzas == legmagasabb:
        nev = x.return_name()
        nyertes.append(nev)
        continue

    else:
        continue

print(set(nyertes))

returnable = " ".join(set(nyertes))
print(f"A legtöbb órát hiányzó tanuló(k): {returnable}")