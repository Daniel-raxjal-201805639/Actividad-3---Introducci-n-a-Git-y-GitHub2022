print ("Mostrar la tabla de multiplicación de un valor ingresado por el usuario.")
num1 = int(input("Ingrese valor para ver tabla de Multiplicar"))
def tabla_multiplicar(num1):
    for i in range(1,11,1):
        print(num1," * ", i, " = ", num1*i)

tabla_multiplicar(num1)