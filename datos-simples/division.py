"""
Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un 
resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> 
son el cociente y el resto de la división entera respectivamente.
"""

n = int(input('Ingrese número entero para el dividendo: '))
m = int(input('Ingrese número entero para el divisor: '))

c = n // m # Resultado del cociente con número entero
r = n % m # Resultado del resto

print(f'Cociente {c}, Resto {r}')