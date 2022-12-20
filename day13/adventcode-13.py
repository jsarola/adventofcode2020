# --- Day 13: Shuttle Search ---
fitxer = open("day-13/bus_timetable.txt","r")

linies = fitxer.readlines()

timestamp = linies[0].strip()

busos = linies[1].split(',')

# Exemple de la primera part
# timestamp = 939
# busos = ['7','13','x','x','59','x','31','19']

# Exemples de la segona part
# busos = ['17','x','13','19']
# busos = ['67','7','x','59','61']
# busos = ['1789', '37', '47', '1889']

print(timestamp, busos)

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

temps_guardat_bus = 0
guardat_bus = 0

# bucle
for temps_bus in busos:
    if is_int(temps_bus):
        modul_bus = int(timestamp) % int(temps_bus)
        temps_proper_bus = int(timestamp) + int(temps_bus) - int(modul_bus)
        if temps_proper_bus < temps_guardat_bus:
            temps_guardat_bus = temps_proper_bus
            guardat_bus = int(temps_bus)
        elif guardat_bus == 0:
            temps_guardat_bus = temps_proper_bus
            guardat_bus = int(temps_bus)

# print(guardat_bus, temps_guardat_bus)

temps_espera = int(temps_guardat_bus) - int(timestamp)
solucio = temps_espera * guardat_bus

print('1 solucio, bus:', guardat_bus, ' temps_espera:', temps_espera, ' -> ', solucio)

# arreglar llista busos amb enters
busos_nou = []
for element in busos:
    if is_int(element):
        busos_nou.append(int(element))
    else:
        busos_nou.append(0)

# ordeno valors per trobar el més gran més fàcil
busos = busos_nou.copy()

busos_ordenats = busos.copy()
busos_ordenats.sort()

print(busos)
print(busos_ordenats)

def comprovar_bus(temps, fets):

    fets = fets + 1
    if fets > len(busos_fets):
        return True

    bus_a_buscar = busos_ordenats[fets * -1]
    posicio = busos.index(bus_a_buscar)

    if bus_a_buscar == 0:
        return True

    modul_bus = int(temps) % int(bus_a_buscar)
    if modul_bus == 0:
        temps_proper_bus = int(temps)
    else:
        temps_proper_bus = int(temps) + int(bus_a_buscar) - int(modul_bus)
    
    if temps_proper_bus == int(temps + posicio):
        # print("correcte", find_bus, temps_proper_bus, temps, posicio)
        # return True
        busos_fets[posicio] = True
        if comprovar_bus(temps, fets):
            return True
        else:
            busos_fets[posicio] = False
            return False
    else:
        # print("no correcte", find_bus, temps_proper_bus, temps, posicio)
        return False

trobat = False

busos_buscar = busos.copy()
busos_fets = [False] * len(busos)

iteracio = 0
max_bus = busos_ordenats[-1]
posicio = busos_buscar.index(max_bus)
# print(posicio, max_bus)

numero_busos = len(busos_buscar) - busos_buscar.count(0)

# print(numero_busos)

log = 0
iteracio = 100000000
while not trobat:
    bus_fet = 1
    tinc_busos = True

    iteracio = iteracio + 1
    # busos_buscar[posicio] = max_bus * iteracio
    # busos_fets[posicio] = True
    temps = max_bus * iteracio - posicio

#    if comprovar_bus(temps, bus_fet):
#        trobat = True

    log = log + 1
    if log % 1000000 == 0:
        print(f'{log:,}')

    # 
    while tinc_busos:
        bus_fet = bus_fet + 1
        
        if bus_fet > numero_busos:
            tinc_busos = False
            trobat = True
            break

        bus_a_buscar = busos_ordenats[bus_fet * -1]
        
        posicio = busos_buscar.index(bus_a_buscar)

        modul_bus = int(temps) % int(bus_a_buscar)
        
        if modul_bus == 0:
            temps_proper_bus = int(temps)
        else:
            temps_proper_bus = int(temps) + int(bus_a_buscar) - int(modul_bus)
    
        if temps_proper_bus == int(temps + posicio):
            pass

            # print("correcte", find_bus, temps_proper_bus, temps, posicio)
            # return True
#            busos_fets[posicio] = True
#            if comprovar_bus(temps, fets):
#                pass #return True
#            else:
#                busos_fets[posicio] = False
#                pass #return False
        else:
            tinc_busos = False
            break
            # print("no correcte", find_bus, temps_proper_bus, temps, posicio)
            # pass #return False



print(busos_buscar, temps)
