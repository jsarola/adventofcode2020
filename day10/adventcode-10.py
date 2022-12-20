# --- Day 10: Adapter Array ---

fitxer = open("adapters.txt","r")

linies = fitxer.readlines()

linies_codi = len(linies)

# print(linies_codi)

llista_jolt = [0] * linies_codi
llista_utilitzada = [False] * linies_codi

llista_ordenada = []

cadena_ordenada = []
for text in linies:
    cadena_ordenada.append(int(text))

llista_ordenada = list(sorted(set(cadena_ordenada)))

# llista_ordenada = [1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49]

print(llista_ordenada, ' - ', len(llista_ordenada))

voltage = 0
suma_1 = 0
suma_3 = 0

for index, numero in enumerate(llista_ordenada):
    # print(index, '-', numero, ' -> ', voltage)
    if int(numero) == int(voltage + 1):
        llista_jolt[index] = 1
        suma_1 = suma_1 + 1
        voltage = voltage + 1
    elif int(numero) == int(voltage + 3):
        llista_jolt[index] = 3
        suma_3 = suma_3 + 1
        voltage = voltage + 3
    else:
        break
# El valor final pot ser:


suma_3 = suma_3 + 1
Producte = suma_1 * suma_3

print('Solucio 1: ', suma_1, suma_3, '=', Producte, ' Voltage final: ', voltage)



solucions = 0

llista_resultat = {}

def acabar_llista(llista):
    retorn = 0
    
    if len(llista) == 1:
        print(llista)
        if (llista[0] +  3) == valor:
            retorn = 1
        elif llista[0] + 2 == valor:
            retorn = 1
        elif llista[0] + 1 == valor:
            retorn = 1
        else:
            retorn = 0
        llista_resultat[str(llista[0])] = retorn
    else:
        valor1 = 0
        valor2 = 0
        valor3 = 0
        calcul1 = False
        calcul2 = False
        calcul3 = False
        if str(llista[0]) not in llista_resultat:
            print ("not in llista 1: ", llista, retorn)
            if llista[0] +  3 in llista:
                index = llista.index(llista[0]+3)
                valor3 = acabar_llista(llista[index:])
                calcul3 = True
            else:
                calcul3 = True
            if llista[0] + 2 in llista:
                index = llista.index(llista[0]+2)
                valor2 = acabar_llista(llista[index:])
                calcul2 = True
            else:
                calcul2 = True
            if llista[0] + 1 in llista:
                index = llista.index(llista[0]+1)
                valor1 = acabar_llista(llista[index:])
                calcul1 = True
            else:
                calcul1 = True
            retorn = valor1 + valor2 + valor3
            if calcul1 and calcul2 and calcul3:
                llista_resultat[str(llista[0])] = retorn
            print ("not in llista 2: ", llista, retorn, llista_resultat)
        else:
            retorn = llista_resultat[str(llista[0])]
            print ("in llista: ", llista, retorn)
        #if len(llista) == 20:
        #    print ('longitut: ', len(llista), 'retorn: ', retorn) 
    return retorn


inputs = linies_codi
# inputs = 7
valor = voltage + 3
# valor = llista_ordenada[inputs-1] + 3

# llista_ordenada = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49]


print(llista_ordenada[:inputs], valor)

# llista_calculada = [0] * inputs
# llista_resultat = [0] * inputs

numero_0 = 0
llista_ordenada.insert(0, numero_0)

solucions = acabar_llista(llista_ordenada)

print(llista_resultat, len(llista_resultat))

print(solucions)