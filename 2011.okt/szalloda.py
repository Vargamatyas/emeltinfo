# 1.feladat
print("adatok beolvasása")
class Adat:

    def __init__(self, sor, sorszam, szoba_szam, erkezes_napja, tavozas_napja, vendegek_szama, reggeli, azonosito):
        self.sor = sor
        self.sorszam = sorszam
        self.szoba_szam = szoba_szam
        self.erkezes_napja = int(erkezes_napja)
        self.tavozas_napja = int(tavozas_napja)
        self.vendegek_szama = int(vendegek_szama)
        self.reggeli = reggeli
        self.azonosito = azonosito
        self.eltoltott_nap = int(self.tavozas_napja) - int(self.erkezes_napja)
        foglaltsag = [x for x in range(int(erkezes_napja), int(tavozas_napja))]
        self.foglalas_intervallum = foglaltsag
        tavasz_vege = 91
        nyar_vege = 213
        fizetendo = 0

        for nap in range(int(erkezes_napja), int(tavozas_napja)):
            if reggeli == "1":
                fizetendo += 1100 * self.vendegek_szama
            if self.vendegek_szama > 2:
                fizetendo += 2000
            if nap < tavasz_vege:
                fizetendo += 9000
            elif tavasz_vege < nap < nyar_vege:
                fizetendo += 10000
            else:
                fizetendo += 8000
        self.fizetnie_kell = fizetendo
        ejszakak = []
        januar = 0
        februar = 0
        marcius = 0
        aprilis = 0
        majus = 0
        junius = 0
        julius = 0
        agusztus = 0
        szeptember = 0
        oktober = 0
        november = 0
        december = 0
        for nap in range(int(erkezes_napja), int(tavozas_napja)):
            if nap < 32:
                januar += 1 * self.vendegek_szama
            if nap < 60:
                februar += 1 * self.vendegek_szama
            if nap < 91:
                marcius += 1 * self.vendegek_szama
            if nap < 121:
                aprilis += 1 * self.vendegek_szama
            if nap <152:
                majus += 1 * self.vendegek_szama
            if nap < 182:
                junius += 1 * self.vendegek_szama
            if nap < 213:
                julius += 1 * self.vendegek_szama
            if nap < 244:
                agusztus += 1 * self.vendegek_szama
            if nap < 274:
                szeptember += 1 * self.vendegek_szama
            if nap < 305:
                oktober += 1 * self.vendegek_szama
            if nap < 335:
                november += 1 * self.vendegek_szama
            else:
                december += 1 * self.vendegek_szama

        if januar == 0:
            pass
        else:
            ejszakak.append(['januar', januar])

        if februar == 0:
            pass
        else:
            ejszakak.append(['februar', februar])

        if marcius == 0:
            pass
        else:
            ejszakak.append(['marcius', marcius])

        if aprilis == 0:
            pass
        else:
            ejszakak.append(['aprilis', aprilis])

        if majus == 0:
            pass
        else:
            ejszakak.append(['majus', majus])

        if junius == 0:
            pass
        else:
            ejszakak.append(['junius', junius])

        if julius == 0:
            pass
        else:
            ejszakak.append(['julius', julius])

        if agusztus == 0:
            pass
        else:
            ejszakak.append(['agusztus', agusztus])

        if szeptember == 0:
            pass
        else:
            ejszakak.append(['szeptember', szeptember])

        if oktober == 0:
            pass
        else:
            ejszakak.append(['oktober', oktober])

        if november == 0:
            pass
        else:
            ejszakak.append(['november', november])

        if december == 0:
            pass
        else:
            ejszakak.append(['december', december])

        self.ejszakak = ejszakak

    def get_eltoltott_nap(self):
        return self.eltoltott_nap

    def get_fizetendo(self):
        return self.fizetnie_kell

    def get_sor(self):
        return self.sor

    def __str__(self):
        return self.azonosito


adatok = []
with open("pitypang.txt") as f:
    foglalasok_szama = f.readline()
    print(foglalasok_szama)
    for line in f:
        sor_tart = line.rstrip().split()
        sor = line.rstrip()
        sorszam = sor_tart[0]
        szoba_szam = sor_tart[1]
        erkezes_nap = sor_tart[2]
        tavozas_nap = sor_tart[3]
        vendegek_szama = sor_tart[4]
        reggeli = sor_tart[5]
        azonosito = sor_tart[6]

        obj = Adat(sor, sorszam, szoba_szam, erkezes_nap, tavozas_nap, vendegek_szama, reggeli, azonosito)
        adatok.append(obj)

# 2.feladat
eltoltott_napok_lista = []

for obj in adatok:
    eltoltott_napok_lista.append(obj.get_eltoltott_nap())

legtobb_elt_nap = eltoltott_napok_lista.index(max(eltoltott_napok_lista))
obj = adatok[legtobb_elt_nap]
print(f"2.feladat:\n{obj.azonosito} {obj.erkezes_napja} - {str(max(eltoltott_napok_lista))}")

# 3.feladat

with open("bevetel.txt", "w") as f:
    for foglalas in adatok:
        f.write(f"{foglalas.sorszam}:{str(foglalas.get_fizetendo())}\n")

teljes_bevetel = 0
for i in adatok:
    teljes_bevetel += i.get_fizetendo()

print(f"3. feladat:\n A szálloda teljes bevétele: {teljes_bevetel} Ft volt")

# 4. feladat
print("4.feladat: ")
januar = 0
februar = 0
marcius = 0
aprilis = 0
majus = 0
junius = 0
julius = 0
agusztus = 0
szeptember = 0
oktober = 0
november = 0
december = 0
eltoltott_ejszakak = [x.ejszakak for x in adatok]

for ejszakakk in eltoltott_ejszakak:
    for i in ejszakakk:
        honap = i[0]
        nap = i[1]

        if honap == 'januar':
            januar += nap
        else:
            pass
        if honap == 'februar':
            februar += nap
        else:
            pass
        if honap == 'marcius':
            marcius += nap
        else:
            pass
        if honap == 'aprilis':
            aprilis += nap
        else:
            pass
        if honap == 'majus':
            majus += nap
        else:
            pass
        if honap == 'junius':
            junius += nap
        else:
            pass
        if honap == 'julius':
            julius += nap
        else:
            pass
        if honap == 'agusztus':
            agusztus += nap
        else:
            pass
        if honap == 'szeptember':
            szeptember += nap
        else:
            pass
        if honap == 'oktober':
            oktober += nap
        else:
            pass
        if honap == 'november':
            november += nap
        else:
            pass
        if honap == 'december':
            december += nap
        else:
            pass
honapok = [januar, februar, marcius, aprilis, majus, junius, julius, agusztus, szeptember, oktober, november, december]
as_str = ["januar", "februar", "marcius", "aprilis", "majus", "junius", "julius", "agusztus", "szeptember", "oktober", "november", "december"]
for index, ho in enumerate(honapok):
    printable = f"{index + 1}: {ho} vendégéj"
    print(printable)

# 5.feladat

sorszama = int(input("kérem adja meg a nap sorszámát"))
napszama = int(input("kérem adja meg az eltöltendő napok számát"))

bekert_adat_intervallum = [x for x in range(sorszama, sorszama + napszama)]

rendelkezesre_allnak = 27

foglalas_intervallum = [nap.foglalas_intervallum for nap in adatok]

for i in bekert_adat_intervallum:
    cond = False
    for intervall in foglalas_intervallum:
        for x in intervall:
            if str(i) == str(x):
                cond = True
            else:
                pass

    if cond is True:
        if rendelkezesre_allnak == 0:
            pass
        else:
            rendelkezesre_allnak -= 1


print(f"a megadott időszak alatt {rendelkezesre_allnak} szoba szabad")



