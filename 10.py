
#10
numero = int(input("ingrese su numero menor a mil "))

if numero < 1000:
    cantidad=len(str(numero)) #len lee la cantidad de digitos y str pasa de caracter a numero para que lean pueda leerlo
    print("el numero tiene " ,cantidad, " de digitos")
else:
    print("El numero ingresado no es inferior a 1000")
    