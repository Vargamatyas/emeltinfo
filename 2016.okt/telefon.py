import math as mt

class Adat:

    def __init__(self,sorszam, hko, hkp, hkmp, bo, bp, bmp):
        self.sorszam = sorszam
        self.hko = int(hko)
        self.hkp = int(hkp)
        self.hkmp = int(hkmp)
        self.bo = int(bo)
        self.bp = int(bp)
        self.bmp = int(bmp)
        self.eredeti_mp = 0
        self.intervallum = []
        self.varakozas_intervallum = []
        self.varakozas_mp = 0

    def return_eredeti_kezdes(self):
        ora = (self.eredeti_mp / 3600)
        ora = mt.floor(ora)
        perc = (self.eredeti_mp - (ora*3600)) / 60
        perc = mt.floor(perc)
        mp = self.eredeti_mp - (ora*3600 + perc * 60)
        return f"{ora} {perc} {mp} "

    def get_eredeti_mp(self):
        return self.eredeti_mp

    def get_varakozas_intervall(self):
        return self.varakozas_intervallum

    def get_intervall(self):
        return self.intervallum

    def set_varakozas_intervallum(self):
        hivaskezdes = self.mpbe(self.hko, self.hkp, self.hkmp)

        self.varakozas_mp = self.eredeti_mp - hivaskezdes

        intervall = []
        for x in range(hivaskezdes, self.eredeti_mp):
            intervall.append(x)

        self.varakozas_intervallum = intervall

    def set_intervallum(self) -> list:
        befejezes = self.mpbe(self.bo, self.bp, self.bmp)
        intervallum = []
        for x in range(self.eredeti_mp, befejezes):
            intervallum.append(x)

        self.intervallum = intervallum

    def hivas_mp_as_eredet(self):
        self.eredeti_mp = self.mpbe(self.hko, self.hkp, self.hkmp)

    def set_eredeti_kezdes(self, eretedeti: int):
        self.eredeti_mp = eretedeti

    def mpbe(self, o, p, mp):

        returnable = o * 3600 + p * 60 + mp

        return returnable

    def get_bef_mp(self) -> int:
        hossz = self.bo * 3600 +  self.bp *60 + self.bmp
        return hossz

    def get_hossz(self):

        hossz = self.mpbe(self.bo, self.bp, self.bmp) - self.mpbe(self.hko, self.hkp, self.hkmp)
        return hossz

    def get_ko(self):
        return int(self.hko)

    def get_sorszam(self):
        return self.sorszam

    def get_varakozas(self):
        return self.varakozas_mp

adatok = []
with open("hivas.txt") as f:
    for index, line in enumerate(f):
        line_list = line.rstrip().split(" ")
        uj_adat = Adat(index+1, line_list[0], line_list[1], line_list[2], line_list[3], line_list[4], line_list[5])
        adatok.append(uj_adat)

adatok[0].hivas_mp_as_eredet()
adatok[0].set_intervallum()
adatok[0].set_varakozas_intervallum()
for x in range(1, len(adatok)):
    elozo_bef = adatok[x-1].get_bef_mp()
    adatok[x].set_eredeti_kezdes(elozo_bef)
    adatok[x].set_intervallum()
    adatok[x].set_varakozas_intervallum()

orak = []

for x in adatok:
    ora = x.get_ko()
    orak.append(ora)



orak_halmaza = list(set(orak))
orak_halmaza.sort()
print(orak_halmaza)

print("3. feladat")
for x in orak_halmaza:
    num = orak.count(x)
    print(f"{x} ora {num} hivas")

hivasszorszam = " "
hossz = 0
print("4.feladat")
for y in adatok:
    aktualis_hossz = y.get_hossz()
    aktualis_sorszam = y.get_sorszam()
    if hossz < aktualis_hossz:
        hossz = aktualis_hossz
        hivasszorszam = aktualis_sorszam
    else:
        continue

print(f"A leghosszabb ideig vonalban levo hivo {hivasszorszam}. sorban szerepel, a hivas hossza: {hossz} masodperc.")

idopont = input("5.feladat: Kérem adjon meg egy időpontot ( Óra perc másodperc formátumban, egy szóközzel tagolva!: ")
idopont = idopont.split(" ")
mpben = int(idopont[0])*3600 + int(idopont[1])*60 + int(idopont[0])

sorszam = 0
for x in adatok:
    intervall = x.get_intervall()
    if mpben in intervall:
        sorszam = x.get_sorszam()

    else:
        continue

vatrakozas = 0
for x in adatok:
    intervall = x.get_varakozas_intervall()
    if mpben in intervall:
        vatrakozas += 1
    else:
        continue

print(f"A varakozok szama: {vatrakozas} a beszelo a {sorszam}. hivo.")

adatok.reverse()

uj_adatok = []
for x in adatok:
    if len(uj_adatok) == 0:
        o = x.get_ko()
        if o < 12 and x.get_eredeti_mp() < x.get_bef_mp():
            uj_adatok.append(x.get_sorszam())
            uj_adatok.append(x.get_varakozas())
        else:
            continue
    else:
        break
print("6.feladat")
print(f"Az utolso telefonalo adatai a(z) {uj_adatok[0]}. sorban vannak, {uj_adatok[1]} masodpercig vart.")

adatok.reverse()
with open("sikeres.txt", "w") as f:
    for x in adatok:
        if x.get_eredeti_mp() < x.get_bef_mp():
            eredeti_or_p_mp = x.return_eredeti_kezdes()
            bo = x.bo
            p = x.bp
            mp = x.bmp
            sorszam = x.get_sorszam()
            f.write(f"{sorszam} {eredeti_or_p_mp} {bo} {p} {mp}\n")



