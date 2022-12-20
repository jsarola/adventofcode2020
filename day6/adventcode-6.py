
fitxer = open("answers.txt","r")

linies = fitxer.readlines()

respostes = []
grup = []

for line in linies:
    if line == "\n":
        #print("Empty Line")
        respostes.append(grup)
        grup=[]
    else:
        grup.append(line.strip())

respostes.append(grup)
 
# print(respostes)
total = 0

for cada_grup in respostes:
    cadena = ""
    for cada_persona in cada_grup:
        cadena = cadena + cada_persona
    # print(cadena)
    cadena_sort = ''.join(sorted(set(cadena)))
    total = total + len(cadena_sort)

print("Total -> ", total)

# print(respostes)
total = 0

for cada_grup in respostes:
    cadena = ""
    primer_pas = True
    resultats = []
    for cada_persona in cada_grup:
        if primer_pas and cadena == "":
            cadena = cada_persona
            primer_pas = False
        else:
            cadena_nova = ""
            for a in cada_persona:
                if a in cadena:
                    cadena_nova = cadena_nova + a
            cadena = cadena_nova
            cadena_sort = ''.join(sorted(set(cadena)))
            if len(cadena) != len(cadena_sort):
                print("problemes")
        resultats.append(cadena)      
    print(resultats)
    # break
    total = total + len(cadena)

print("Total -> ", total)