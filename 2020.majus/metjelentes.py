class Nap:
    def __init__(self):
        self.adatok = []
        self.varosok = []
    def add_adat(self, adat):
        self.adatok.append(adat)

    def get_utolso_meresi_adat(self, varos_kod):
        self.adatok.reverse()
        temp_list = []
        for x in self.adatok:
            if x.get_telepules() == varos_kod:
                temp_list.append(x.get_ido_ora_perc())

        utolso_idopont = temp_list[0]
        self.adatok.reverse()
        return utolso_idopont

    def get_minho(self):
        homersekletek = [x.get_ho() for x in self.adatok]
        min_ho = min(homersekletek)
        min_index = homersekletek.index(min_ho)
        megfelelo_adat = self.adatok[min_index]
        return [megfelelo_adat.get_telepules(), megfelelo_adat.get_ido_ora_perc(), megfelelo_adat.get_ho()]

    def get_maxho(self):
        homersekletek = [x.get_ho() for x in self.adatok]
        max_ho = max(homersekletek)
        max_index = homersekletek.index(max_ho)
        megfelelo_adat = self.adatok[max_index]
        return [megfelelo_adat.get_telepules(), megfelelo_adat.get_ido_ora_perc(), megfelelo_adat.get_ho()]

    def show_szelcsend(self):
        szelcsend = []
        for x in self.adatok:
            szelcsend_adat = x.get_szelcsend()
            if szelcsend_adat is None:
                continue
            szelcsend.append(szelcsend_adat)

        if len(szelcsend) == 0:
            print("Nem volt szélcsend a mérések idején.")
        else:
            for x in szelcsend:
                print(x)

    def gen_city_set(self):
        varosok = [x.get_telepules() for x in self.adatok]
        self.varosok = list(set(varosok))

    def show_kozephok(self):
        orak = []
        hok = []
        osszes_ho = []
        for c in self.varosok:
            for x in self.adatok:

                if c == x.get_telepules():
                    osszes_ho.append(x.get_ho())
                    orak.append(x.get_ora())
                    if x.get_ora() == "1" or "7" or "13" or "19":
                        hok.append(x.get_ho())

            if "1" and "7" and "13" and "19" in orak:
                kozepho = self.kozephok(hok)
            else:
                kozepho = "NA"
            hoing = self.ho_ing(osszes_ho)
            print(f"{c} Középhőmérséklet: {kozepho}; Hőmérséklet-ingadozás: {hoing}")
            orak = []
            hok = []
            osszes_ho = []

    def kozephok(self, lista):
        ho = 0
        for x in lista:
            ho += int(x)
        ho = ho / (len(lista))
        return round(ho)

    def ho_ing(self, lista):
        minimum = min(lista)
        maximum = max(lista)
        hoing = int(maximum) - int(minimum)
        return hoing

    def create_file(self):
        for c in self.varosok:
            with open(c + ".txt", "w") as f:
                f.write(c + "\n")
                for x in self.adatok:
                    if c == x.get_telepules():
                        ido = x.get_ido_ora_perc()
                        szelerosseg = "#" * int(x.get_erosseg())
                        f.write(f"{ido} {szelerosseg}\n")



class Adat:
    def __init__(self, telepules, ido, szeliranyeserosseg, ho):
        self.telepules = telepules
        self.ido = ido
        self.ora = self.ido[:2]
        self.perc = self.ido[2:]
        self.idopont = self.ora + ":" + self.perc
        self.szeliranyeserosseg = szeliranyeserosseg
        self.szelirany = szeliranyeserosseg[:2]
        self.erosseg = szeliranyeserosseg[3:]
        self.ho = ho

    def get_ora(self):
        return self.ora

    def get_telepules(self):
        return self.telepules

    def get_ido_ora_perc(self):
        return self.ora + ":" + self.perc

    def get_ho(self):
        return self.ho

    def get_szelcsend(self):
        if str(self.szeliranyeserosseg) == "00000":
            return self.telepules + " " + self.idopont
        else:
            pass

    def get_erosseg(self):
        return self.erosseg

nap = Nap()
with open("tavirathu13.txt") as f:
    for line in f:
        sor = line.rstrip().split(" ")
        uj_adat = Adat(sor[0], sor[1], sor[2], sor[3])
        nap.add_adat(uj_adat)

nap.gen_city_set()
# 2.feladat
varos_kod = input("2. feladat\nAdja meg egy település kódját! Település: ")
utolso_idopont = nap.get_utolso_meresi_adat(varos_kod)
print(f"Az utolsó mérési adat a megadott településről {utolso_idopont}-kor érkezett")

# 3.feladat
minimum = nap.get_minho()
print(f"A legalacsonyabb hőmérséklet: {minimum[0]} {minimum[1]} {minimum[2]} fok.")
maximum = nap.get_maxho()
print(f"A legmagasabb hőmérséklet: {maximum[0]} {maximum[1]} {maximum[2]} fok.")

# 4.feladat
nap.show_szelcsend()

# 5.feladat
print("5. feladat")
nap.show_kozephok()

# 6. feladat

nap.create_file()