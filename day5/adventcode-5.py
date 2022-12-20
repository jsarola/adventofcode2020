import re
import math

fitxer = open("boarding_passes.txt","r")

linies = fitxer.readlines()

seat_final = 0

# Crear 
llista_ocupats = ["L"]* 8 * 128 

# totes les linies
for cadena in linies:
    # separar files i columnes
    fila = cadena[:7]
    columna = cadena[7:]
    # print("fila/columna", fila, "/", columna)

    # per cada caràcter de la fila comprovar el número
    # treballo de la 1 a la 128 per fer els càlculs mes senzills
    pos_ini = 1
    pos_fi = 128
    temp = 128
    for caracter in fila:
        temp = temp / 2
        if caracter == "F":
            pos_fi = pos_fi - temp
        elif caracter == "B":
            pos_ini = pos_ini + temp
        else:
            pass
        # print("caracter -> pos_ini/pos_fi",caracter, "->", pos_ini, "/", pos_fi)

    fila_final = pos_ini - 1

    # per cada caràcter de la columna comprovar el número
    # treballo de la 1 a la 8 per fer els càlculs mes senzills
    pos_ini = 1
    pos_fi = 8
    temp = 8
    for caracter in columna:
        temp = temp / 2
        if caracter == "L":
            pos_fi = pos_fi - temp
        elif caracter == "R":
            pos_ini = pos_ini + temp
        else:
            pass
        # print("caracter -> pos_ini/pos_fi",caracter, "->", pos_ini, "/", pos_fi)

    columna_final = pos_ini - 1

    seat_id = fila_final * 8 + columna_final

    print("boarding -> fila + columna : seat_id", cadena.strip(), " -> ", fila_final, "+", columna_final, ' : ', seat_id, " ", llista_ocupats[int(fila_final * 8 + columna_final)])
    llista_ocupats[int(fila_final * 8 + columna_final)] = 'O'


    if seat_final < seat_id:
        seat_final = seat_id
   

print("seat final ID: ", seat_final)

pos = 0
for cadira in llista_ocupats:
    if cadira == "L":
        fila = math.trunc(pos / 8)
        columna = pos - (fila * 8)
        print("fila/columna - ", fila, columna)
    pos = pos + 1


