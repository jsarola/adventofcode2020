
fitxer = open("luggage.txt","r")

linies = fitxer.readlines()

respostes = []
grup = []

bosses = []

def trobar_color(color_que_busquem, quines_bosses):
    color_trobat = []
    
    color_trobat.append(color_que_busquem)
    for colors in quines_bosses:
        # print(colors[0])
        # print(colors[1])
        for fulla in colors[1]:
            # print(fulla)
            if color_que_busquem in fulla:
                # print(colors)
                llista_trobat = trobar_color(colors[0], quines_bosses)
                # print("llista_trobat: ", llista_trobat)
                if len(llista_trobat) > 0:
                    color_trobat = color_trobat + llista_trobat
    return color_trobat


for line in linies:
    nou_grup =[]
    grup = line.split("contain")
    color_bossa = grup[0]
    color_bossa = color_bossa.split("bag")[0].strip()

    nou_grup.append(color_bossa)

    color_contingut = []
    for contingut in grup[1].split(","):
        llista_tmp = []
        valors = contingut.split()
        if valors[0] != "no":
            color_dins = valors[1] + " " + valors[2]
            unitats = valors[0]
            llista_tmp.append(color_dins)
            llista_tmp.append(unitats)
        # print(llista_tmp)
        color_contingut.append(llista_tmp)
    
    # print(color_contingut)
    nou_grup.append(color_contingut)
    # print(color_bossa, " - ", color_contingut)
    bosses.append(nou_grup)

# print(bosses)

color_a_buscar = 'shiny gold'

flatlist = trobar_color(color_a_buscar, bosses)
# print(flatlist, len(flatlist))
# sortlist = sorted(flatlist)
sortlist = list(sorted(set(flatlist)))
# Menys 1 perque afegeixo el que busco a la llista, i aquest no compte
print(sortlist, len(sortlist) - 1)


def buscar_bossa(color_que_busquem, quines_bosses):
          
    num_bossa = 1

    for colors in quines_bosses:
        # print(color_que_busquem, colors[0])
        color_trobat = colors[0]
        if color_que_busquem == color_trobat:            
            for fulla in colors[1]:
                #num_bossa = num_bossa + buscar_bossa(fulla[0], quines_bosses)*int(fulla[1])
                # print("fulla ->", fulla)
                if len(fulla) > 0:
                    color_a_buscar = fulla[0]
                    quantes_bosses = int(fulla[1])
                    num_bossa = num_bossa + quantes_bosses * buscar_bossa(color_a_buscar, quines_bosses)                    
                # print("fulla ->", fulla, " ", num_bossa)
            print("fulla ->", colors[0], "->", colors[1], " = ", num_bossa)
    return num_bossa


color_a_buscar = 'shiny gold'

number_bosses = buscar_bossa(color_a_buscar, bosses)

# He de restar la primera
print("quantes bosses -> ", number_bosses - 1)
