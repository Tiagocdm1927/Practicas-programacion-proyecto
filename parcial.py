raiz = []
respuesta = input("desea ingresar un numero a la lista?")
while respuesta == "si":
    numero = int(input("ingrese el numero"))
    raiz.append(numero)
print(raiz)
for i in range(1, numero + 1):
    suma = suma + 1