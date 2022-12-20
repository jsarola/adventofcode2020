
fitxer = open("instructions.txt","r")

linies = fitxer.readlines()

linies_codi = len(linies)

executades = [ False ] * linies_codi

posicio = 0
acumulat = 0

while posicio < linies_codi:
    posicio_inicial = posicio
    if executades[posicio]:
        break
    
    cadena = linies[posicio].split()
    operacio = cadena[0]
    argument = int(cadena[1].strip())
    # print(operacio, argument)

    executades[posicio] = True

    if operacio == 'acc':
        acumulat = acumulat + argument
        posicio = posicio + 1
    elif operacio == 'jmp':
        posicio = posicio + argument
    elif operacio == 'nop':
        posicio = posicio + 1
    else:
        pass

    # print("Operacio: ", posicio_inicial, " ", cadena, " Posicio seguent: ", posicio, ' Acumulat: ', acumulat, ' ', executades[posicio])
    
    if posicio == linies_codi:
        break

print("Valor acumulat 1: ", acumulat)


canviades = [ False ] * linies_codi

final = False
while not final:
    posicio = 0
    acumulat = 0

    executades = [ False ] * linies_codi
    un_canvi = False
    while posicio < linies_codi:
        posicio_inicial = posicio
        if executades[posicio]:
            break
    
        cadena = linies[posicio].split()
        operacio = cadena[0]
        argument = int(cadena[1].strip())
        # print(operacio, argument)

        executades[posicio] = True

        if operacio == 'acc':
            acumulat = acumulat + argument
            posicio = posicio + 1
        elif operacio == 'jmp':
            if canviades[posicio] or un_canvi:
                posicio = posicio + argument                
            else:
                canviades[posicio] = True
                posicio = posicio + 1                
                un_canvi = True
        elif operacio == 'nop':
            if canviades[posicio] or un_canvi:
                posicio = posicio + 1                
            else:
                canviades[posicio] = True
                posicio = posicio + argument                
                un_canvi = True
        else:
            pass

        # print("Operacio: ", posicio_inicial, " ", cadena, " Posicio seguent: ", posicio, ' Acumulat: ', acumulat, ' ', executades[posicio_inicial], '-', canviades[posicio_inicial])

        #if posicio > 650:
            #print("LINIA: ", posicio)
    
        if posicio == linies_codi:
            final = True 
            break

print("Valor acumulat 2: ", acumulat)