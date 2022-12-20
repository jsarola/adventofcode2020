# --- Day 16: Ticket Translation ---

fitxer = open("day-16/ticket_translation.txt","r")

linies = fitxer.readlines()

nearby_tickets = []
for linia in linies:
    trobar = linia.strip()
    trobar_list = trobar.split(',')
    trobar_list_int = [int(i) for i in trobar_list] 
    nearby_tickets.append(trobar_list_int)

your_tickets = [139,113,127,181,53,149,131,239,137,241,89,151,109,73,157,59,107,83,173,179]

# print(len(nearby_tickets))

departure_location = list(range(30,828+1)) + list(range(839,971+1))
departure_station = list(range(38,339+1)) + list(range(352,958+1))
departure_platform = list(range(39,905+1)) + list(range(921,968+1))
departure_track = list(range(36,570+1)) + list(range(586,972+1))
departure_date = list(range(48,190+1)) + list(range(196,957+1))
departure_time = list(range(29,483+1)) +  list(range(491,963+1))
arrival_location = list(range(28,779+1)) + list(range(803,959+1))
arrival_station = list(range(27,221+1)) + list(range(238,966+1))
arrival_platform = list(range(28,732+1)) + list(range(741,963+1))
arrival_track = list(range(41,752+1)) + list(range(767,967+1))
lclass = list(range(27,437+1)) + list(range(452,972+1))
duration = list(range(38,93+1)) + list(range(107,958+1))
price = list(range(36,196+1)) + list(range(213,974+1))
route = list(range(48,858+1)) + list(range(880,956+1))
row = list(range(36,59+1)) + list(range(73,974+1))
seat = list(range(39,423+1)) + list(range(431,974+1))
train = list(range(38,499+1)) + list(range(518,958+1))
ttype = list(range(45,562+1)) + list(range(569,961+1))
wagon = list(range(28,161+1)) + list(range(171,959+1))
zone = list(range(44,75+1)) + list(range(83,964+1))

diccionari = {}
diccionari[1] = departure_location
diccionari[2] = departure_station
diccionari[3] = departure_platform
diccionari[4] = departure_track
diccionari[5] = departure_date
diccionari[6] = departure_time
diccionari[7] = arrival_location
diccionari[8] = arrival_station
diccionari[9] = arrival_platform
diccionari[10] = arrival_track
diccionari[11] = lclass
diccionari[12] = duration
diccionari[13] = price
diccionari[14] = route
diccionari[15] = row
diccionari[16] = seat
diccionari[17] = train
diccionari[18] = ttype
diccionari[19] = wagon
diccionari[20] = zone


def xxx_comprovar_numero(llista, posicio):
    correcte = True
    numero = llista[posicio]
    # print("INICI ", posicio, numero)

    llista_dolent = []
    dicc_correcte = []
    
    quin = 0
    fer_bucle = True
    while fer_bucle:
        quin = quin + 1
        if quin not in dicc_correcte:
            if numero in diccionari[quin]:
                dicc_correcte.append(quin)
                # print(dicc_correcte, quin, numero)
                if posicio == len(llista)-1:
                    correcte = True
                    fer_bucle = False
                else:
                    comprovat = xxx_comprovar_numero(llista, posicio + 1)
                    if comprovat:
                        correcte = True
                        fer_bucle = False
                    else:
                        correcte = False
                        fer_bucle = False
            else:
                llista_dolent.append(numero)
                correcte = False
                fer_bucle = False
        if quin == len(llista):
            fer_bucle = False

    return correcte


# your_tickets = [1,113,127,181,53,149,131,239,137,241,2,151,109,73,157,59,107,83,173,179]

def comprovar_numero(numero):
    correcte = False
    for i in range(1,21):
        if numero in diccionari[i]:
            correcte = True
            break

    return correcte

total = 0

nova_llista = []

for la_llista in nearby_tickets:

    es_bo = True
    for element in la_llista:
        if not comprovar_numero(element):
            es_bo = False
            total = total + element

    if es_bo:
        nova_llista.append(la_llista)

print("La solucio 1 es: ", total)

print("length", len(nova_llista))

tiquets = len(nova_llista)
dic_comprovats = []
dic_llistes = list(range(0,len(nova_llista[0])))

print(dic_llistes)

def comprovar_diccionari(quin):
    comprovat = True
    for llistes in dic_llistes:
        for pos in range(len(nova_llista)):
            element = nova_llista[pos][llistes]
            if element not in diccionari[quin]:
                comprovat = False
                break
        if comprovat:
            dic_llistes.pop(llistes)
            retorn = comprovar_diccionari(quin + 1)
            if not retorn:
                dic_llistes.append(llistes)
                comprovat = False
                break

    return comprovat

llista_dicc = []
eldiccionari = 1
acabar = False
while not acabar:
    acabar = comprovar_diccionari(eldiccionari)
    if acabar:
        break
    else:
        eldiccionari = eldiccionari + 1

print(llista_dicc)

#            
#    dicc_correcte = []
#    llista_dolent = []
#    acabar = False
#    llista_buscar = la_llista.copy()
#    while not acabar:
#        if comprovar_numero(llista_buscar, 0):
#            acabar = True
#        else:
#            llista_buscar = []
#            for element in la_llista:
#                if element not in llista_dolent:
#                    llista_buscar.append(element)
#    

#    print(llista_dolent, sum(llista_dolent))
    
#    total = total + sum(llista_dolent)        


# def comprovar_llista(llista):
#     acabat = false
#     index = 0
#     dicc_correcta = []
#     while not acabat:
#         quin_dicc = comprovar_numero(llista[index])
#         if diccionari > 1:
#             dicc_correcte.append(quin_dicc)
#         if len(dicc_correcte) == 20:
#             acabat = True
#         elif 
#         comprovar_numero(llista[index])
#         
# 
# 
# for llista in nearby_tickets:
#     dicc_correte = []
# 
#     for numero in llista:
#         buscar_opcio(numero)
