fitxer = open('arbres.txt', 'r')

linies = fitxer.readlines()


suma_linia=len(linies)

final=0
fila=[]
for linia in linies:
    fila.append(linia[:-1])
    final=final+1

pfila=2
pcol=1

llista=[[1,1],[1,3],[1,5],[1,7],[2,1]]

for elements in llista:
    pfila = elements[0]
    pcol = elements[1]
    fila=[]
    for linia in linies:
        fila.append(linia[:-1])
        final=final+1

    while pfila<suma_linia:
        # print(str(pfila)+"-"+str(pcol))
        while len(fila[pfila]) <= pcol:
            cadena=fila[pfila]
            cadena2= cadena+fila[pfila]
            fila[pfila]=cadena2
        if fila[pfila][pcol]=="#":
            cadena=fila[pfila]
            cadena=cadena[:pcol]+"X"+cadena[pcol+1:]
            fila[pfila]=cadena
        else:
            cadena=fila[pfila]
            cadena=cadena[:pcol]+"O"+cadena[pcol+1:]
            fila[pfila]=cadena
        
        pfila=pfila+elements[0]
        pcol=pcol+elements[1]

    arbres=0
    pfila=1
    while pfila<suma_linia:
        #if fila[pfila].count("X")>0:
            # print(fila[pfila])
        arbres=arbres + fila[pfila].count("X")
        pfila=pfila+1

    print("arbres " + str(elements[0]) + "/" + str(elements[1]) + " -> " + str(arbres))

