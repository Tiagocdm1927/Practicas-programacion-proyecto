#11
numero = int(input("Ingrese un numero: "))

suma = 0

for i in range(1, numero + 1): #recorre los numeros desde el 1 hasta el numero ingresado

    if i % 2 != 0: #Saca todos los impar de los numeros 
        suma = suma + i # suma los impares 

print("La suma es:", suma)

if suma % 2 == 0:
    print("Es par")

else:
    print("Es impar")