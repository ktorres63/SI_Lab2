#CIFRADOR
archivo = "testDescifrar.txt"
#archivo = input("ingrese el nombre del archivo: ")
try:
    file = open(archivo,'r')
    alphaC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    cont = file.read().upper()
    #desp = int(input("ingrese desplazamiento: "))
    desp = 3
    textcifr=""

    #C = M +3 mod 27
    
    for c in cont:
        if c in alphaC:
            indice = (alphaC.index(c) - desp) % 27
            textcifr += alphaC[indice]
        else:
            continue


    print(cont)
    print(textcifr)

except FileNotFoundError:
    print("El archivo no existe")