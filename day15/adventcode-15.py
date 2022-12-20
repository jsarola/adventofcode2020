# --- Day 15: Rambunctious Recitation ---

import time

puzzle = [15, 12, 0, 14, 3, 1]

# puzzle =[0, 3, 6]

iteracio = 0
last_number = 0

max_iteracio = 30000000
spoken = []
eldiccionari = {}

acabo = False

start = time.time()

def afegir_iteracio(numero, afegir):
    if numero in eldiccionari:
        if len(eldiccionari[numero]) > 1:
            eldiccionari[numero].pop(0)
            eldiccionari[numero].append(afegir)
        else:
            eldiccionari[numero].append(afegir)
    else:            
        llista = [afegir]
        eldiccionari[numero] = llista

for iteracio in range(1, (max_iteracio + 1)):

    if iteracio <= len(puzzle):
        # print('inici', iteracio, '->', last_number, spoken)
        spoken.append(puzzle[iteracio-1])
        last_number = puzzle[iteracio-1]
        afegir_iteracio(last_number, iteracio)
        
        # print('Llegits:    ', spoken)
        # print('Diccionari: ', eldiccionari)
    else:
        if last_number in eldiccionari:  # spoken.count(last_number) > 1:
            if len(eldiccionari[last_number]) > 1:
                elements = eldiccionari[last_number]
                # print('Elements: ', elements, '-', last_number)
                if len(elements) > 1:
                    # print('exist', iteracio, '->', last_number, spoken)
                    pos_ini = elements[0]
                    pos_fin = elements[1]                
                # trobats = False
                # index = len(spoken)
                # while not trobats:
                #     index = index - 1
                #     if spoken[index] == last_number:
                #         # print ('trobat')
                #         if pos_fin == 0:
                #             pos_fin = index
                #         elif pos_ini == 0:
                #             pos_ini = index
                #             trobats = True
                #         else:
                #             print("error")
                #             exit()                
                # # print(pos_fin, pos_ini)
                    spoken.append(pos_fin - pos_ini)
                    last_number = pos_fin - pos_ini
                    afegir_iteracio(last_number, iteracio)
                    
                else:
                    spoken.append(0)
                    last_number = 0
                    afegir_iteracio(last_number, iteracio)                    
            else:
                spoken.append(0)
                last_number = 0                
                afegir_iteracio(last_number, iteracio)
                
        # print('Llegits:    ', spoken)
        # print('Diccionari: ', eldiccionari)

    
    if iteracio % 10000 == 0:
        print('Iteracio:',iteracio, ': ', "{:.2f}".format(time.time() - start), ' (last_number:',last_number,')')
        # print('Llegits:    ', spoken)
        # print('Diccionari: ', eldiccionari)
      

    #if iteracio == max_iteracio:
        # print('Llista -> ', spoken)
    #    acabo = True

# [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]

print('Solucio: ', last_number)
