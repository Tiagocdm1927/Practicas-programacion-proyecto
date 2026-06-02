#8
parcial_1 = int(input("ingrese su nota de su primer parcial "))
parcial_2 = int(input("ingrese su nota del segundo parcial "))
parcial_3 = int(input("ingrese su tercer parcial "))
integrador = int(input("ingrese su nota en el integrador "))
final = int(input("ingrese su nota en el trabajo final "))

total_parciales = ( (parcial_1 + parcial_2 + parcial_3) / 3 ) * 55 / 100
total_integrador = integrador * 30 / 100
total_final = final * 15 /100
nota_final = total_final + total_integrador + total_parciales
if nota_final >= 6:
    print("Usted aprobo")
else:
    print("Usted no aprobo")