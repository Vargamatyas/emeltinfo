# 1.feladat
with open("sms.txt") as f:
    mai_napi_uzenetek = f.readline().rstrip()
    sorok = []
    for line in f:
        sorok.append(line.rstrip())


class Uzenet:
    def __init__(self, erk_ora, erk_perc, tel_szam, uzenet):
        self.erk_ora = erk_ora
        self.erk_perc= erk_perc
        self.tel_szam = tel_szam
        self.uzenet = uzenet
        self.uzenet_hossza = len(uzenet)
        self.intervallumban = self.get_intervallum()

    def get_uzenet(self):
        return self.uzenet

    def get_uzenet_hossz(self):
        return self.uzenet_hossza

    def get_ora(self):
        return self.erk_ora

    def get_perc(self):
        return self.erk_perc

    def get_t_szam(self):
        return self.tel_szam

    def get_intervallum(self):
        intervallumok = [[x for x in range(1, 21)], [y for y in range(21, 41)], [g for g in range(41, 61)],
                         [z for z in range(61, 81)], [p for p in range(81, 100)]]

        for index, u in enumerate(intervallumok):
            if self.uzenet_hossza in u:
                if index == 0:
                    return "1_20"
                if index == 1:
                    return "21_40"
                if index == 2:
                    return "41_60"
                if index == 3:
                    return "61_80"
                if index == 4:
                    return "81_100"


adatok = []
for p in range(0, len(sorok), 2):
    elso_sora = sorok[p].split(" ")
    masodik_sor = sorok[p + 1]

    adat = Uzenet(elso_sora[0], elso_sora[1], elso_sora[2], masodik_sor)
    adatok.append(adat)

# 2.feladat
friss_uzenet = adatok[len(adatok) - 1].get_uzenet()
print(f"2. feladat: A legfrissebb üzenet a {friss_uzenet}")

# 3.feladat
uzenetek_hossza = [x.get_uzenet_hossz() for x in adatok]
min_index = adatok[uzenetek_hossza.index(min(uzenetek_hossza))]
max_index = adatok[uzenetek_hossza.index(max(uzenetek_hossza))]
print(f"3.feladat:\nA leghosszabb üzenet {max_index.get_ora()} órakkor {max_index.get_perc()} perckor a {max_index.get_t_szam()} számról érkezett, az üzenet: {max_index.get_uzenet()}")
print(f"A legrövidebb üzenet {min_index.get_ora()} órakkor {min_index.get_perc()} perckor a {min_index.get_t_szam()} számról érkezett, az üzenet: {min_index.get_uzenet()}")

# 4.feladat
print("4. feladat: ")

egy_husz = 0
husz_negyven = 0
negyven_hatvan = 0
hatvan_nyolcvan = 0
nyolcvan_szaz = 0

for i in adatok:
    intervall = i.get_intervallum()

    if intervall == "1_20":
        egy_husz += 1

    if intervall == "21_40":
        husz_negyven += 1

    if intervall == "41_60":
        negyven_hatvan += 1

    if intervall == "61_80":
        hatvan_nyolcvan += 1

    if intervall == "81_100":
        nyolcvan_szaz += 1
print(f"1-20 {egy_husz} db 21-40 {husz_negyven} db 41-60 {negyven_hatvan} db 61-80 {hatvan_nyolcvan} db 81-100 {nyolcvan_szaz} db")

# 5.feladat

olvasatlan = 0
orak = [x for x in range(0, 25)]

for i in orak:
    uzenet_per_ora = 0
    for u in adatok:
        if u.get_ora() == i:
            uzenet_per_ora += 1
        else:
            continue

    vegleges = uzenet_per_ora - 10
    if vegleges > 0:
        olvasatlan += vegleges
    else:
        continue

print(f"5. feladat: {olvasatlan} db uzenetert kellene felhivnia a szolgaltatot.")

# 6.feladat

counter = 0
for b in adatok:
    if b.get_t_szam() == "123456789":
        counter += 1
if counter < 2:
    print("nincs elegendő üzenet")

else:
    legnagyobb = 0

    for index, b in enumerate(adatok):
        if b.get_t_szam() == "123456789":
            for c in adatok[:index]:
                if c.get_t_szam() == "123456789":

                    b_ido = int(b.get_ora()) * 60 + int(b.get_perc())
                    c_ido = int(c.get_ora()) * 60 + int(c.get_perc())
                    ido_telt = b_ido - c_ido
                    print(ido_telt)

                    if ido_telt > legnagyobb:
                        legnagyobb = ido_telt

    if legnagyobb > 60:
        ora = int((str(legnagyobb / 60).split("."))[0])
        print(f"az ora {ora}")
        perc = legnagyobb - (ora * 60)
        ido = f"{ora} óra {perc} perc"
    else:
        ido = f"{legnagyobb} perc"

    print(f"6. feladat: A legtöbbb idő ami eltelt: {ido}")

# 7.feladat
input_uzenet = input(f"7. feladat kérem adja meg sorrendben az órát, a percet, a telefonszámot szóközökkel tagolva!: ").split()
uzenet = input("add meg az uzenetet: ")
ora = input_uzenet[0]
perc = input_uzenet[1]
szam = input_uzenet[2]


uj_adat = Uzenet(ora, perc, szam, uzenet)
adatok.append(uj_adat)

telefonszamok = list(set([x.get_t_szam() for x in adatok]))
telefonszamok.sort()
print(telefonszamok)

with open("smski.txt", "w") as f:
    for c in telefonszamok:
        f.write(f"{c}\n")
        for p in adatok:
            szam = p.get_t_szam()
            if szam == c:
                f.write(f"{p.get_ora()} ora {p.get_perc()} perc {p.get_uzenet()}\n")
            else:
                continue

