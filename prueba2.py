print("Que producto desea comprar?")
print("ingrese 1 para teclado, 2 para mouse, 3 para pantallas")
Respuesta = int(input("4 para salir "))
suma = 0
while Respuesta != 4:
    if Respuesta == 1:
        teclado = int(input("que teclado desea comprar? de 100$,200$ o 300$?"))
        suma = suma + teclado
    elif Respuesta ==2:
        mouse = int(input("que mouse desea comprar? 100$,200$ o 300$"))
        suma = suma + mouse
    elif Respuesta ==3:
        pantalla = int(input("que pantalla desea comprar? 100$,200$ o 300$?"))
        suma = suma + pantalla
    elif Respuesta ==4:
        print("usted a salido de la pagina web")
    else:
        print("opcion incorrecta")
    Respuesta = int(input("Que desea hacer ahora? 1 teclado, 2 mouse, 3 pantalla, 4 salir"))
print("su total a pagar es ", suma,)