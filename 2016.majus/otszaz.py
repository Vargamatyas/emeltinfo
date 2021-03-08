class Kosar:
    def __init__(self):
        self.kosar = []
        self.fizetendo = 0

    def get_fizetendo(self):
        return self.fizetendo

    def add_to_cart(self, item):
        self.kosar.append(item)

    def calculate_fizetendo(self):
        kosar_copy = self.kosar

        items = set(kosar_copy)
        for x in items:
            mennyiseg = self.kosar.count(x)
            if mennyiseg == 1:
                self.fizetendo += 500

            if mennyiseg == 2:
                self.fizetendo += 950

            if mennyiseg > 2:
                self.fizetendo += 950
                mennyiseg -= 2
                self.fizetendo += mennyiseg * 400

    def count_items_in_kosar(self):
        db_item = len(self.kosar)
        return db_item

    def find_item(self, item):
        db_item = self.kosar.count(item)
        return db_item

    def print_kosar(self):
        copy = self.kosar
        set_copy = list(set(copy))
        for x in set_copy:
            db = self.kosar.count(x)
            print(f"{db} {x}")


def ertek(db):
    osszeg = 0
    if db == 1:
        osszeg = 500
    if db == 2:
        osszeg = 950
    if db > 2:
        osszeg = 950
        db -= 2
        osszeg += db * 400

    return osszeg

vasarlok = []

txt_tartalma = []
with open("penztar.txt") as f:
    for line in f:
        sor = line.rstrip()
        txt_tartalma.append(sor)

aktualis_kosar = []
for x in txt_tartalma:
    if x != "F":
        aktualis_kosar.append(x)
    else:
        new_kosar = Kosar()
        for x in aktualis_kosar:
            new_kosar.add_to_cart(x)
        aktualis_kosar = []
        vasarlok.append(new_kosar)

# 2. feladat
print(f"2. feladat: {len(vasarlok)} db fizetés történt")

# 3. feladat
print(f"3. feladat: Az első vásárló: {vasarlok[0].count_items_in_kosar()} db árucikket vásárolt.")

# 4. feladat
print("4. feladat")

vasarlas_sorszama = int(input("Kérem adja meg a vásárlás sorszámát: ")) + 1
arucikk_neve = input("Kérem adja meg az árucikk nevét: ")
db_szam = int(input("Kérem adjon meg egy darabszámot: "))

elofordult_db = 0
for x in vasarlok:
    elofordult_db += x.find_item(arucikk_neve)

eloszor = "nem fordult elő"
utoljara = "nem fordult elő"
for index, y in enumerate(vasarlok):
    if arucikk_neve in y.kosar:
        if eloszor == "nem fordult elő":
            eloszor = index
            utoljara = index
        else:
            if index > utoljara:
                utoljara = index
if eloszor != "nem fordult elő":
    eloszor += 1
    utoljara += 1
print(f"5. feladat: Az árucikket először a {eloszor}.-ik vásárlásnál, utoljára a {utoljara}.-ik vásárlásnál vették, összesen {elofordult_db} szor vettek belőle")

print(f"6. feladat: A bekért darabszámot vásárolva: {ertek(db_szam)} - Ft-ot kellene fizetni.")

kivalasztott_vasarlo = vasarlok[vasarlas_sorszama]
print("7. feladat: ")
kivalasztott_vasarlo.print_kosar()

with open("osszeg.txt", "w") as f:
    for index, x in enumerate(vasarlok):
        x.calculate_fizetendo()
        fizetes = x.get_fizetendo()
        printable = f"{index + 1}: {fizetes}"
        f.write(printable + "\n")


