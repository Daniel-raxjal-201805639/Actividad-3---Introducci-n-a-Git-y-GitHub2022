print ("Indicar cuantas vocales hay en un texto.")
texto = input ("Ingrese un texto: ")
contador = 0
for i in texto:
    if i == 'a' or i == 'e' or i == 'i' or i =='o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i =='O' or i == 'U':
        contador = contador+1
        vocal = contador
print ("La cantidad de vocales es de: ", vocal)