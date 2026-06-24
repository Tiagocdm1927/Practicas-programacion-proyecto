#def añadir (numero):
#   lista = []
#    for i in range(numero):
#        añadir=int(input("ingrese el numero que desea añadir "))
#        lista.append(añadir)
#    return lista
#numero = int(input("ingrese cuantos numeros desea añadir "))
#resultado = añadir(numero)
#print(resultado)


#def añadir (numero):
#    lista = []
#    for i in range(numero):
#        nuevo_numero = int(input("ingrese su numero "))
#        lista.append(nuevo_numero)
#    return sum(lista)

#numero = int(input("Ingrese cuantos numeros desea añadir "))
#resultado =añadir(numero)
#print(resultado)



#def añadir(numero):
#    lista = []
#    for i in range(numero):
#        nuevo_numero = int(input("ingrese su numero "))
#        lista.append(nuevo_numero)
#    return max(lista)

#numero = int(input("ingrese cuantos numeros desea añadir"))

#resultado = añadir(numero)
#print(resultado)
#def par(numero):
#    lista = []
#    suma = 0
#    for i in range(numero):
#        añadir = int(input("ingrese que numero desea agregar "))
#        lista.append(añadir)
#    for numero in lista:
#        if numero % 2 == 0:
#            suma = suma + 1
#    return lista, suma

#numero = int(input("ingrese cuantos numeros desea añadir "))
#lista, pares = par(numero)
#print("los numeros pares en total son ", pares)

#def sumar ():
#    numero_1 = int(input("ingrese el primer numero "))
#    numero_2 =int(input("ingrese el segundo numero "))
#    return numero_1 + numero_2

#def restar():
#    numero_1 = int(input("ingrese el primer numero "))
#    numero_2 =int(input("ingrese el segundo numero "))
#    return numero_1 - numero_2

#def dividir ():
#    numero_1 = int(input("ingrese el primer numero "))
#    numero_2 =int(input("ingrese el segundo numero "))
#    return numero_1 / numero_2

#def multiplicar():
#    numero_1 = int(input("ingrese el primer numero "))
#    numero_2 =int(input("ingrese el segundo numero "))
#    return numero_1 * numero_2


#calculadora = int(input("ingrese 1 para sumar, 2 para restar, 3 para dividir, 4 para multiplicar y 5 para salir "))
#while calculadora<6:
#    if calculadora == 1:
#        resultado = sumar()
#        print("Su resultado es " ,resultado)
#        calculadora = int(input("desea realizar otra operacion? 1 para sumar, 2 para restar, 3 para dividir, 4 para multiplicar y 5 para salir"))
#    elif calculadora ==2:
#        resultado = restar()
#        print("Su resultado es " ,resultado)
#        calculadora = int(input("desea realizar otra operacion?"))
#    elif calculadora ==3:
#        resultado = dividir()
#        print("Su resultado es " ,resultado) 
#        elif calculadora ==4:
#        resultado = multiplicar()
#        print("Su resultado es " ,resultado)
#        calculadora = int(input("desea realizar otra operacion?"))
#    elif calculadora ==5:
#        print("saliendo de la calculadora")
#        calculadora == 100
#    elif calculadora >=6:
#        print("resultado incorrecta ")
#        calculadora == int(input("1 para sumar, 2 para restar, 3 para dividir, 4 para multiplicar y 5 para salir"))


def entrada(cantidad):
    nro = input(" Ingrese un número entero: ")
    m = nro
    p=0
    for i in range(1, cantidad):
        nro = int(input(f" Ingrese el {i+1} ° numero entero: "))
        if nro > m:
            m = nro
            p=i
    return m,p		  #¿qué es m?    

cantidad = input("Ingrese una cantidad de números: ")
m,p = entrada(cantidad)
print(f"El número que está buscando es el {m} y se encuentra en la posición {p} ")    
