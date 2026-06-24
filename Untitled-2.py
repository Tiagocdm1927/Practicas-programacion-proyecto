def prueba(lista):

    total = 0

    for numero in lista:
        if numero % 2 != 0:
            total += numero

    return total

print(prueba([1, 2, 3, 4, 5]))

