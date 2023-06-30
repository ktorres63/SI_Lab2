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

def preProcASCII(text): #ASCII characters
    textP = ""
    for c in text:
        textP += c
    return textP


def ciphASCII(key, text):
    txtCiph = ""

    #Ci=(Mi+Ki)%191
    for i in range(len(text)):
        m = ord(text[i])
        k = ord(key[i])

        tmp = (m+k) % 191
        txtCiph+=chr(tmp)
    return txtCiph

def ciphVS(key, text):
    alpha = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    txtCiph = ""

    #Ci=(Mi+Ki)%27
    for i in range(len(text)):
        m = alpha.index(text[i])
        k = alpha.index(key[i])
        tmp = (m+k) % 27
        txtCiph+=alpha[tmp]
    return txtCiph


def nKey(key, sizeW):
    nKey = ""
    for i in range(sizeW):
        nKey += key[i % len(key)]
    return nKey


def frecuencias(text):
    freq = {}
    alpha = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for i in range(len(alpha)):
        frecuenc = text.count(alpha[i])
        freq[alpha[i]] = frecuenc

    # Imprimir la tabla de frecuencias
    for letra, frecuencia in freq.items():
        print(f"Letra '{letra}': {frecuencia} veces")


#archivo = input("ingrese el nombre del archivo: ")
archivo = "testCifrar.txt"
try:
    file = open(archivo, 'r')
    #contRaw = file.read()
    cont = file.read()
    contUpp = cont.upper()

    #alpha = input("seleccione (1) para cifrar en alfabeto de 27 o (2) para cifrar en alfabeto de 191: ")
    alpha = "1"

    key = input("ingresa la clave: ").upper()
    #key = "MEZCLADOR"
    match alpha:
        case "1":  # 27 letras
            tProc = preProcAlpha(contUpp)
            nkey = nKey(key, len(tProc))
            print(tProc)
            txtCipher = ciphVS(nkey, tProc)
            print(txtCipher)
            frecuencias(txtCipher)

        case "2":

            tProc = preProcASCII(cont)
            nkey = nKey(key, len(tProc))
            print(tProc)
            print(nkey)

            print(ciphASCII(nkey, tProc))

        case _:
            print("ingrese un numero valido")

    file.close()
except FileNotFoundError:
    print("El archivo no existe")
