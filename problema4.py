print ("Indicar cual de 3 valores es el mayor")
num1 = int(input("Ingrese un número:"))
num2 = int(input("Ingrese un número:"))
num3 = int(input("Ingrese un número:"))
if num1>num2:
    if num1>num3:
        print (num1," es mayor")
    else:
        print (num3," es mayor")
else:
    if num2>num3:
        print (num2, "es mayor ")
    else:
        print (num3," es mayor")