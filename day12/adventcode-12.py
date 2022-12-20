# --- Day 12: Rain Risk ---

fitxer = open("evasive_actions.txt","r")

linies = fitxer.readlines()

linies_codi = len(linies)

print(linies_codi)


actions = []
for cada_linia in linies:
    accio = [cada_linia[0], int(cada_linia[1:].strip())]
    actions.append(accio)

# actions = [['F', 10], ['N', 3], ['F', 7], ['R', 90], ['F', 11]]

def validar(angle, rotacions):
    angles = [0, 90, 180, 270]
    index = angles.index(angle)
    angle_final = int((index + rotacions) % 4)

    return angles[angle_final]

east = 0
nord = 0
face = 0

for accio in actions:
    # print ('PRE  -> ', 'E-', east, ' N-', nord, ' FACE-', face)
    if accio[0] == 'N':
        nord = nord + accio[1]
    elif accio[0] == 'S':
        nord = nord - accio[1]
    elif accio[0] == 'E':
        east = east + accio[1]
    elif accio[0] == 'W':
        east = east - accio[1]
    elif accio[0] == 'L':
        rotacions = accio[1] / 90
        face = validar(face, rotacions)
    elif accio[0] == 'R':
        rotacions = accio[1] / 90
        face = validar(face, rotacions* -1)
    elif accio[0] == 'F':
        if face == 0:
            east = east + accio[1]
        elif face == 90:
            nord = nord + accio[1]
        elif face == 180:
            east = east - accio[1]
        elif face == 270:
            nord = nord - accio[1]
        else:
            pass
    else:
        pass
    # print ('POST -> ', 'E-', east, ' N-', nord, ' FACE-', face)

print('1 -> MANHATTAN = ', abs(east) + abs(nord))

east = 0
nord = 0
weast = 10
wnord = 1
face = 0

def validarRotacio(eastpos, nordpos, rotacions):
    pos_east = 0
    pos_south = 0
    pos_west = 0
    pos_nord = 0

    if rotacions == 1 or rotacions == -3:
        pos_south = eastpos
        pos_east = nordpos
    elif rotacions == 2 or rotacions == -2:
        pos_west = eastpos
        pos_south = nordpos
    elif rotacions == 3 or rotacions == -1:
        pos_nord = eastpos
        pos_west = nordpos

    return [int(pos_east - pos_west), int(pos_nord - pos_south)]

for accio in actions:
    # print ('PRE  -> ', 'E-', east, ' N-', nord, ' FACE-', face)
    if accio[0] == 'N':
        wnord = wnord + accio[1]
    elif accio[0] == 'S':
        wnord = wnord - accio[1]
    elif accio[0] == 'E':
        weast = weast + accio[1]
    elif accio[0] == 'W':
        weast = weast - accio[1]
    elif accio[0] == 'L':
        rotacions = accio[1] / 90
        tmp_weast = validarRotacio(weast, wnord, rotacions * -1)[0]
        tmp_wnord = validarRotacio(weast, wnord, rotacions * -1)[1]
        weast = tmp_weast
        wnord = tmp_wnord
    elif accio[0] == 'R':
        rotacions = accio[1] / 90
        tmp_weast = validarRotacio(weast, wnord, rotacions)[0]
        tmp_wnord = validarRotacio(weast, wnord, rotacions)[1]
        weast = tmp_weast
        wnord = tmp_wnord
    elif accio[0] == 'F':
        east = east + accio[1]*weast
        nord = nord + accio[1]*wnord
    else:
        pass
    # print ('POST -> ', 'WE-', weast, ' WN-', wnord)
    # print ('POST -> ', 'E-', east, ' N-', nord)

print('2 -> MANHATTAN = ', abs(east) + abs(nord))