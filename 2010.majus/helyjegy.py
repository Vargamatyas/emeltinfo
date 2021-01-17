# 10km utan 10 ft
# eladott jegyek száma 500
# vonal hossz max 200

class Utas:
    def __init__(self, idnum, ules, starting_km, ending_km, ossz_km, forint_per_km):
        self.idnum = idnum
        self.ules = ules
        self.starting_km = starting_km
        self.ending_km = ending_km
        self.utazott_tav = ending_km - starting_km
        self.busz_uttav = ossz_km
        self.forint_per_km = forint_per_km
        self.utazasi_intervallum = [int(x) for x in range(self.starting_km, self.ending_km + 1)]

    def get_utas_intervallum(self):
        return self.utazasi_intervallum

    def set_utolso_megallo(self, utolso_megallo):
        self.utolso_megallo = utolso_megallo

    def get_utolso_hellyen_leszallo(self):
        cond = False
        if self.ending_km == self.utolso_megallo:
            cond = True

        return cond


    def get_ending_km(self):
        return self.ending_km

    def get_jegyar(self):

            megkezdett = int((str(self.utazott_tav / 10).split("."))[0]) + 1
            fizetendo = megkezdett * self.forint_per_km
            if fizetendo % 5 == 0:
                return fizetendo
            else:
                return round(fizetendo)

    def vegig_utazta(self):
        cond = False
        if self.utazott_tav == self.busz_uttav:
            cond = True

        return cond

    def get_utazott_tav(self):
        return self.utazott_tav

    def get_ules(self):
        return self.ules

    def get_id(self):
        return self.idnum


# 1.feladat

utasok = []
with open("eladott.txt") as f:

    elso_sor = f.readline().rstrip().split(" ")
    eddig_eladott_jegyek = elso_sor[0]
    km = elso_sor[1]
    forint_tiz_km = elso_sor[2]

    for index, line in enumerate(f):
        sor = line.rstrip().split(" ")
        utas = Utas(index + 1, sor[0], int(sor[1]), int(sor[2]), int(km), int(forint_tiz_km))
        utasok.append(utas)

# 2.feladat
utolso_utas = utasok[-1]
returnable = [utolso_utas.get_ules(), utolso_utas.get_utazott_tav()]
print(f"2.feladat: Az utolsó utas a {returnable[0]} hellyen ült, {returnable[1]} kilómétert utazott.")

# 3.feladat
vegig_utaztak = []
for elem in utasok:
    cond = elem.vegig_utazta()
    if cond is True:
        vegig_utaztak.append(str(elem.get_id()))
    else:
        pass

if len(vegig_utaztak) == 0:
    print("3.feladat: Senki sem utazta végig a távot")
else:
    printable = " ".join(vegig_utaztak)
    print(f"3.feladat A {printable} sorszámú utasok végig utazták a teljes távot.")

# 4.feladat
osszeg = 0
for i in utasok:
    osszeg += int(i.get_jegyar())

print(f"4.feladat: A teljes bevétel: {osszeg} Ft")

# 5.feladat
busz_megallok = []

for i in utasok:
    leszallo_km = i.get_ending_km()
    if leszallo_km not in busz_megallok:
        busz_megallok.append(leszallo_km)
    else:
        continue
busz_megallok.sort()
utolso_megallo = busz_megallok[-1]
utolso_megalloban_szalltak = 0

for i in utasok:
    i.set_utolso_megallo(utolso_megallo)

for i in utasok:
    feltetel = i.get_utolso_hellyen_leszallo()
    if feltetel is True:
        utolso_megalloban_szalltak += 1

print(f"5.feladat: {utolso_megalloban_szalltak} utas szállt le az utolsó megállóban.")

# 6.feladat

megallok_szama = len(busz_megallok)

if 200 in busz_megallok:
    megallok_szama -= 1

print(f"6.feladat {megallok_szama} hellyen állt meg a busz.")

# 7.feladat

pont = int(input("7.feladat: Kérem adja meg a kiindulástól mért távolságot: "))

hash_map = {"0": "test"}
utasok_szama = len(utasok)

for i in range(1, 49):
    cond = False
    for index, y in enumerate(utasok):
        utas_intervall = y.get_utas_intervallum()

        if int(pont) in utas_intervall and int(y.get_ules()) == i: # and y.get_ending_km() not in busz_megallok:
            if y.get_ending_km() == pont:
                continue
            hash_map[f"{i}"] = f"{y.get_id()}. utas"
            cond = True

    if cond is False:
        hash_map[f"{str(i)}"] = "ures"

print(hash_map)

with open("kihol.txt", "w") as f:
    for i in range(1, 49):
        szekszam_allapota = hash_map.get(str(i))
        f.write(f"{i}. ulesen: {szekszam_allapota}\n")
