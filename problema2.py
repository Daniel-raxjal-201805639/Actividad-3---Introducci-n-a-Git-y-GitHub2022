import math
print("Calcular la hipotenusa de un triángulo rectángulo")
cateto1 = float(input('Ingrese el primer cateto'))
cateto2 = float(input('Ingrese el segundo cateto'))
hipo = math.sqrt((cateto1**2)+(cateto2**2))
print("la hipotenusa es de: ",hipo)
