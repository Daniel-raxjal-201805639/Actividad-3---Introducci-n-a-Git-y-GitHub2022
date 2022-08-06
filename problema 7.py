print ("Mostrar cuantas veces se repite la letra S en un texto ingresado por el usuario.")
import re
texto = input("Ingrese texto: ")

print('Repeticiones de S', len(re.findall('s', texto)))