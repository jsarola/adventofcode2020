import re

fitxer = open("passports.txt","r")

linies = fitxer.readlines()

passport = []
cadena = ""

for line in linies:
    if line == "\n":
        #print("Empty Line")
        passport.append(cadena)
        cadena=""
    else:
        if cadena == "":
            cadena = line.strip()
        else:
            cadena = cadena + " " + line.strip()
passport.append(cadena)
cadena=""

#print(passport[4])

llista_busca = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #, "cid"]

passaport_bo = 0
passaport_dolent = 0

print(passport[0])
print(passport[len(passport)-1])

for passaport in passport:
    trobat = 0
    variable = []
    posicio = []
    for busca in llista_busca:
        posicio_busca = passaport.find(busca)
        posicio.append(posicio_busca)
        if passaport.find(busca)>=0:
            trobat = trobat + 1
            variable.append(busca) 
    if trobat > 6:
        passaport_bo = passaport_bo + 1
        # print(passaport)
    else:
        passaport_dolent = passaport_dolent + 1
        #print(passaport + " - " + str(trobat) + " - ")
        #print(variable)
        #print(posicio)

print("Passaports bons son:" + str(passaport_bo))
print("Passaports dolents son:" + str(passaport_dolent))

passaport_bo = 0
passaport_dolent = 0

colors_ulls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

patro_hcl = re.compile('#[a-f0-9]{6}')
patro_pid = re.compile('[0-9]{9}')

for passaport in passport:
    trobat = 0
    variable = []
    posicio = []
    cadena_pass = passaport.split()
    cadena_bona = []
    for trobar in cadena_pass:
        cadena_bona.append(trobar.split(":"))
    
    for trobar in cadena_bona:
        if 'byr' in trobar:
            es_bo = False
            year = int(trobar[1])
            if year >= 1920 and year <= 2002:
                es_bo = True
                trobat = trobat + 1
            # print(trobar, " -> ", es_bo)
        if 'iyr' in trobar:
            es_bo = False
            year = int(trobar[1])
            if year >= 2010 and year <= 2020:
                es_bo = True
                trobat = trobat + 1
            # print(trobar, " -> ", es_bo)
        if 'eyr' in trobar:
            es_bo = False
            year = int(trobar[1])
            if year >= 2020 and year <= 2030:
                es_bo = True
                trobat = trobat + 1
            # print(trobar,  " -> ", es_bo)
        if 'hgt' in trobar:
            es_bo = False
            tmp = trobar[1]
            unitat = int(tmp.find("cm"))
            if unitat >= 0:
                hgt = int(tmp[:(len(tmp)-2)])
                if hgt >= 150 and hgt <= 193:
                    es_bo = True
                    trobat = trobat + 1
            unitat = int(tmp.find("in"))
            if unitat >= 0:
                hgt = int(tmp[:(len(tmp)-2)])
                if hgt >= 59 and hgt <= 76:
                    es_bo = True
                    trobat = trobat + 1
            # print(trobar, " -> ", hgt, "-", es_bo)
        if 'hcl' in trobar:
            es_bo = False
            # print("hcl -> " + str(re.search(patro_hcl, trobar[1])))
            if re.fullmatch(patro_hcl, trobar[1]):
                es_bo = True
                trobat = trobat + 1
            # print(trobar, " -> ", es_bo)
        if 'ecl' in trobar:
            es_bo = False
            if trobar[1] in colors_ulls:
                es_bo = True
                trobat = trobat + 1
            # print(trobar, " -> ", es_bo)
        if 'pid' in trobar:
            es_bo = False
            # print("pid -> " + str(re.match(patro_pid, trobar[1])))
            if re.fullmatch(patro_pid, trobar[1]):
                es_bo = True
                trobat = trobat + 1
            # print(trobar, " -> ", es_bo)

    if trobat > 6:
        passaport_bo = passaport_bo + 1
        print("Bo ", passaport)
    else:
        passaport_dolent = passaport_dolent + 1
        #print(passaport + " - " + str(trobat) + " - ")
        #print(variable)
        #print(posicio)
        # print("Dolent ", passaport)

print("Passaports bons son:" + str(passaport_bo))
print("Passaports dolents son:" + str(passaport_dolent))
