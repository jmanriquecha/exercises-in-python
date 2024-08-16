# Contador de vocales

cadena = input('Ingrese cualquier texto y el programa contara cuantas vocales tiene: ').strip().lower()
contador = 1

for i in range(len(cadena)):
    if cadena[i] == 'a' or cadena[i] == 'e' or cadena[i] == 'i' or cadena[i] == 'o' or cadena == 'u':
        contador += 1
    else:
        continue
print(contador)