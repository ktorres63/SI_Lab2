def preProcAlpha(text):  # 27 characters
    textP = ""
    for c in text:
        if c == " " or c == ",":
            continue
        elif c == "Á":
            textP += "A"
        elif c == "É":
            textP += "E"
        elif c == "Í":
            textP += "I"
        elif c == "Ó":
            textP += "O"
        elif c == "Ú":
            textP += "U"
        else:
            textP += c

    return textP


def desCiphVS(key, textC):
    alpha = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    txt = ""

    # Mi=(Ci-Ki)%27
    for i in range(len(textC)):
        c = alpha.index(textC[i])
        k = alpha.index(key[i])
        tmp = (c-k) % 27

        txt += alpha[tmp]
    return txt


def nKey(key, sizeW):
    nKey = ""
    for i in range(sizeW):
        nKey += key[i % len(key)]
    return nKey


# archivo = input("ingrese el nombre del archivo: ")
archivo = "testDescifrar.txt"
try:
    file = open(archivo, 'r')
    # contRaw = file.read()
    cont = file.read()
    contUpp = cont.upper()

    #key = input("ingresa la clave: ").upper()
    key = "PEDRONAVAJA"

    tProc = preProcAlpha(contUpp)
    nkey = nKey(key, len(tProc))
    print(tProc)
    txtDesCipher = desCiphVS(nkey, tProc)
    print(txtDesCipher)

    file.close()
except FileNotFoundError:
    print("El archivo no existe")
