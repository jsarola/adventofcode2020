# --- Day 9: Encoding Error ---
fitxer = open("encoding.txt","r")

linies = fitxer.readlines()

linies_codi = len(linies)

posicio = 0
acumulat = 0

trobat = False
posicio = 25

while not trobat:
    buscar = int(linies[posicio])
    suma_trobada = False
    for i in range(posicio-25,posicio-1):
        valor_i = int(linies[i])
        for j in range(i+1,posicio):
            valor_j = int(linies[j])
            suma = valor_i + valor_j
            # print(i, "-", j, "->", suma)
            if suma == buscar:
                suma_trobada = True
    
    if not suma_trobada:
        break
    posicio = posicio + 1

print("Resultat 1: ", buscar)

trobat = False

for i in range(posicio-1):
    valor_i = int(linies[i])
    suma = valor_i
    llista_suma = []
    llista_suma.append(valor_i)
    
    for j in range(i+1,posicio):
        valor_j = int(linies[j])
        llista_suma.append(valor_j)
        suma = suma + valor_j
        # print(i, "-", j, "->", suma)
        
        if suma == buscar:
            suma_trobada = True
            break
    
    if suma_trobada:
        break

print(llista_suma)
sortlist = list(sorted(set(llista_suma)))
petit = int(sortlist[0]) 
gran = int(sortlist[len(sortlist)-1])
suma = petit + gran
print("Petit =", petit, " Gran = ", gran, " SUMA= ", suma)
