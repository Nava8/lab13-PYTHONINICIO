def es_par(numero):
    return numero % 2 == 0

def es_impar(numero):
    return numero % 2 != 0


def retorna_pares(inicio , fin):
    pares = []
    for numero in range(inicio , fin+1):
        if numero % 2 == 0:
            pares.append(numero)
    return pares