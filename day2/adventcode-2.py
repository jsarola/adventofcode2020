
fitxer = open('passwords.txt', 'r')

linies = fitxer.readlines()

count = 0
bona = 0
bona2 = 0
for fila in linies:
    count = count + 1
    print("Line{}: {}".format(count, fila.strip()))
    lafila = fila.split()
    min_car = int(lafila[0].split('-')[0])
    max_car = int(lafila[0].split('-')[1])
    lletra = lafila[1][:1]
    contrasenya = lafila[2]
    print(min_car, max_car, lletra, contrasenya)

    comptar = contrasenya.count(lletra)
    if comptar >= min_car and comptar <= max_car:
        bona = bona + 1
        print("BONA!")

    char1 = contrasenya[min_car-1]
    char2 = contrasenya[max_car-1]
    print(char1, "-", char2)
    correcte = 0
    if char1 == lletra:
        correcte = 1
    if char2 == lletra:
        correcte = correcte + 1
    if correcte == 1:
        bona2 = bona2 + 1
        print("BONA - 2!")


print("bones: ", bona)
print("bones2: ", bona2)