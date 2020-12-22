# 1. feladat
print("1. feladat")

jarmu_txt_allomany = []
ido_k = []
rendszamok = []
with open("jarmu.txt") as f:
    for line in f:
        line_content = line.rstrip().split(" ")
        jarmu_txt_allomany.append(line_content)
        ido_k.append([line_content[0], line_content[1], line_content[2]])
        rendszamok.append(line_content[3])

# 2. feladat
print("2. feladat:")
orak =  []
kezdo_ora = 0

for i in ido_k:
    ora = int(i[0])
    if ora > kezdo_ora:
        orak.append(ora)
        kezdo_ora = ora
    else:
        continue


print( "aznap legalább {0} órát  dolgoztak az ellenőrzést végzők".format(len(orak)))

# 3. feladat
print("3. feladat")
orak = []
elso_kocsik = []
kezdo_ora = 0

for index, i in enumerate(ido_k):
    ora = int(i[0])
    if ora > kezdo_ora:
        elso_kocsik.append(rendszamok[index])
        orak.append(ora)
        kezdo_ora = ora
    else:
        continue

for index, ora in enumerate(orak):
    print("{0} óra: {1}".format(ora, elso_kocsik[index]))

# 4. feladat
print("4. feladat")
autobusz = 0
kamion = 0
motor = 0
szemelygepkocsi = 0
for rendszam in rendszamok:
    aktualis_rendszam = list(rendszam)[0]
    if aktualis_rendszam == "B":
        autobusz += 1
    if aktualis_rendszam == "K":
        kamion += 1
    if aktualis_rendszam == "M":
        motor += 1
    else:
        szemelygepkocsi += 1

print("Autobuszból: {0}, kamionból: {1}, motorból: {2}, személygépkocsiból: {3} haladt el.".format(
    str(autobusz), str(kamion), str(motor), str(szemelygepkocsi)
))

# 5. feladat
print("5. feladat")

intervallum = []
idotartam = 0
# 1 ora = 3600 mp
elemek_szama = len(ido_k)

for index, ido in enumerate(ido_k):
    if elemek_szama - 1 == index:
        break
    else:
        kezdo_ora_list = list(ido)

        kezdo_oraa ="{0}:{1}:{2}".format(kezdo_ora_list[0], kezdo_ora_list[1], kezdo_ora_list[2])
        tol_ora = list(ido)[0]
        tol_perc = list(ido)[1]
        tol_mp = list(ido)[2]

        veg_ora_list = list(ido_k[index + 1])
        veg_ora = "{0}:{1}:{2}".format(veg_ora_list[0], veg_ora_list[1], veg_ora_list[2])
        ig_ora = int(list(ido_k[index + 1])[0])
        ig_perc = int(list(ido_k[index + 1])[1])
        ig_mp = int(list(ido_k[index + 1])[2])

        vegleges_ora = ig_ora - int(tol_ora)
        vegleges_perc = ig_perc - int(tol_perc)
        vegleges_mp = ig_mp - int(tol_mp)

        ideiglenes_idotartam = (vegleges_ora * 3600) + (vegleges_perc * 60) + vegleges_mp
        if ideiglenes_idotartam > idotartam:
            idotartam = ideiglenes_idotartam
            intervallum = [kezdo_oraa, veg_ora]
        else:
            pass

print("A leghosszabb forgalommentes időszak: {0} - {1}".format(intervallum[0], intervallum[1]))


print("6. feladat")
lehetseges_rendszam = list(input("kérjem adja meg a rendszámot"))

rendszamok_egyezhetnek = []
for rendszam in rendszamok:
    rendszam_list = list(rendszam)
    possible_solution = []
    for index,i in enumerate(lehetseges_rendszam):
        if i == "*":
            possible_solution.append("*")
            continue
        else:
            if i == rendszam_list[index]:
                possible_solution.append(i)
                continue
            else:
                continue
    if len(possible_solution) == 7:
        rendszamok_egyezhetnek.append(rendszam)
    else:
        continue

print("Ezek a rendszámok lehetnek a sémára illeszthetők: {0}".format(" ,".join(rendszamok_egyezhetnek)))

# 7.feladat
print("7.feladat")
# mivel a legnagyobb forgalom mentes idopontban is 5perc alatt volt a forgalomhiany, ezért:
ellenorizhetok = []
viszonyitasiszam = 0
for index, i in enumerate(ido_k):
    if len(ellenorizhetok) == 0:
        ellenorizhetok.append(index)
        viszonyitasiszam = (int(i[0]))*3600 + (int(i[1]))*60 + int(i[2]) * 1
    else:
        aktualis_ido = (int(i[0]))*3600 + (int(i[1]))*60 + int(i[2]) * 1

        if aktualis_ido < viszonyitasiszam + (5 * 60):
            pass
        else:
            ellenorizhetok.append(index)
            viszonyitasiszam = aktualis_ido

with open("vizsgalt.txt", "w") as f:
    for i in ellenorizhetok:
        irando_str = " ".join(list(jarmu_txt_allomany[int(i)]))
        f.write(irando_str  + "\n")







