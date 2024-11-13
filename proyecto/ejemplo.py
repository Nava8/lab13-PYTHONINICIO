import modulo3

def longitud():
    palabra = input("Ingrese la palabra que quiere saber su longitud: ")
    long = modulo3.longitud_texto(palabra)
    print(f"La palabra '{palabra}' tiene una longitud de {long} caracteres.")

longitud()
