'''
Imprimir triángulo simétrico de la siguiente forma
Usuario proporciona un valor. Ejem. 3
Se dibuja el siguiente triangulo.add()

  *
 ***
*****
'''

numero_filas = int(input('Ingrese el número de filas: '))

for fila in range(1, numero_filas + 1):
    espacios_blanco = ' ' * (numero_filas - fila) # Formula calcula espacios en blanco
    asteriscos = '*' * (2 * fila - 1)
    print(f'{espacios_blanco}{asteriscos}')