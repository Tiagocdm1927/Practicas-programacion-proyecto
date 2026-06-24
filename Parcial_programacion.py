#10

hora = 250.50
horas_trabajadas = int(input("ingrese el total de horas trabajadas "))
total = hora*horas_trabajadas
print("su total de sueldo es " ,total)


#11
def parcial():
    total_parciales = ( (parcial_1 + parcial_2 + parcial_3) / 3 ) * 55 / 100
    return total_parciales

def integrador_final():
    total_integrador = integrador * 30 / 100
    return total_integrador

def nota_():
    total_final = final * 15/100
    return total_final


parcial_1 = int(input("ingrese su nota de su primer parcial "))
parcial_2 = int(input("ingrese su nota del segundo parcial "))
parcial_3 = int(input("ingrese su tercer parcial "))
integrador = int(input("ingrese su nota en el integrador "))
final = int(input("ingrese su nota en el trabajo final "))

final_parcial = parcial()
final_integrador = integrador_final()
total_final = nota_()
nota_final = total_final + final_integrador + final_parcial
if nota_final >= 6:
    print("Usted aprobo")
else:
    print("Usted no aprobo")

#13
numero = int(input("ingrese su numero menor a mil "))

if numero < 1000:
    cantidad=len(str(numero)) 
    print("el numero tiene " ,cantidad, " de digitos")
else:
    print("El numero ingresado no es inferior a 1000")
    

#14
numero = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(1, numero + 1):
    suma = suma + i
print("La suma es:", suma)