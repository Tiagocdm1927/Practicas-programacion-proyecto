nombres = ["Messi", "Ronaldo", "Neymar"]
buscar = input("ingrese el nombre que desea buscar ")
if buscar in nombres:
    posicion = nombres.index(buscar) ## busca la posicion de la variable "buscar" en la lista "nombres" y lo asigna a la variable "posicion"
    print("la posicion de ", buscar, " esta en la numero " ,posicion)
else:
    print("el jugador colocado no esta en la lista")