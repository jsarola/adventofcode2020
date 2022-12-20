# --- Day 11: Seating System ---

fitxer = open("seats.txt","r")

linies = fitxer.readlines()

linies_codi = len(linies)

print(linies_codi)

def split(word): 
    return [char for char in word]  

seats = []
for cada_linia in linies:
    seats_line = split(cada_linia.strip())
    seats.append(seats_line)

num_files = len(seats)
num_columnes = len(seats[0])

seats_original = seats

def ocupats(cadires, x, y):
    suma = 0
    if x == 0:
        fila_in = 0
        fila_fi = x + 2
    elif x + 1 == num_files:
        fila_in = x - 1
        fila_fi = x + 1
    else:
        fila_in = x - 1
        fila_fi = x + 2
    if y == 0:
        col_in = 0
        col_fi = y + 2
    elif y + 1 == num_columnes:
        col_in = y - 1
        col_fi = y + 1
    else:
        col_in = y - 1
        col_fi = y + 2
    
    for a in range(fila_in, fila_fi):
        for b in range(col_in, col_fi):
            # print("-> ", a, "-", b, ":", cadires[a][b])
            if a == x and b == y:
                pass
            elif cadires[a][b] == "#":
                suma = suma + 1
            else:
                pass
    
    return suma

hi_ha_canvis = True
iteracions = 0
while hi_ha_canvis:
    hi_ha_canvis = False
    seats_new = []
    for i, fila in enumerate(seats):
        seats_line_new = []
        for j, columna in enumerate(fila):
            seients_ocupats = ocupats(seats, i, j)
            # print(i,'-', j, '-', columna, ':', seients_ocupats)
            if columna == ".":
                seats_line_new.append(".")
            elif columna == "L":
                if seients_ocupats == 0:
                    seats_line_new.append("#")
                    hi_ha_canvis = True
                else:
                    seats_line_new.append("L")
            else:
                if seients_ocupats >= 4:
                    seats_line_new.append("L") 
                    hi_ha_canvis = True
                else:
                    seats_line_new.append("#") 
        seats_new.append(seats_line_new)
    
    if hi_ha_canvis:
        iteracions = iteracions + 1
        #if iteracions == 2:
        #    hi_ha_canvis = False

    print('Iteracions: ', iteracions)
    seats = seats_new

print(seats)

seients = 0
for fila in seats:
    for columna in fila:
        if columna == "#":
            seients = seients + 1
        
print('1 -> Seients ocupats: ', seients)

def diagonal(cadires, x, y, a, b):

    fil = x
    col = y

    valor = 0
    trobat = False

    while not trobat:
        fil = fil + a
        col = col + b        
        if 0 <= fil < num_files:
            if 0 <= col < num_columnes:
                if cadires[fil][col] == 'L':
                    trobat = True
                    valor = 0                    
                elif cadires[fil][col] == '#':
                    trobat = True
                    valor = 1
                else:
                    pass
            else:
                trobat = True
                valor = 0
        else:
            trobat = True
            valor = 0
    
    return valor

def ocupatsdiagonal(cadires, x, y):

    ocupats = 0

    diagonals = [[-1, -1], [0, -1], [+1, -1], [-1, 0], [+1, 0],[-1, +1], [0, +1], [+1,+1]]

    for opcions in diagonals:        
        ocupats = ocupats + diagonal(cadires, x, y, opcions[0], opcions[1])
        # print(x, y, opcions[0], opcions[1], ocupats)

    return ocupats

seats = seats_original

hi_ha_canvis = True
iteracions = 0
while hi_ha_canvis:
    hi_ha_canvis = False
    seats_new = []
    for i, fila in enumerate(seats):
        seats_line_new = []
        for j, columna in enumerate(fila):
            seients_ocupats = ocupatsdiagonal(seats, i, j)
            # print(i,'-', j, '-', columna, ':', seients_ocupats)
            if columna == ".":
                seats_line_new.append(".")
            elif columna == "L":
                if seients_ocupats == 0:
                    seats_line_new.append("#")
                    hi_ha_canvis = True
                else:
                    seats_line_new.append("L")
            else:
                if seients_ocupats >= 5:
                    seats_line_new.append("L") 
                    hi_ha_canvis = True
                else:
                    seats_line_new.append("#") 
        seats_new.append(seats_line_new)
    
    if hi_ha_canvis:
        iteracions = iteracions + 1
        #if iteracions == 2:
        #    hi_ha_canvis = False

    print('Iteracions: ', iteracions)
    seats = seats_new

print(seats)

seients = 0
for fila in seats:
    for columna in fila:
        if columna == "#":
            seients = seients + 1

print('2 -> Seients ocupats: ', seients)