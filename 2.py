a = 2
b = 3
c = 5
resultado = 0
pregunta = int(input("Que desea hacer? 1 para +, 2 para -, 3 para /, 4 para *"))
if pregunta==1:
    print(a+b+c)
elif pregunta==2:
    print(a-b-c)
elif pregunta==3:
    print(a/b/c)
elif pregunta ==4: 
    print(a*c*b)
else:
    print("el numero ingresado no es valido")