print('*** Comprensión de listas ***')
# Sintaxis comprensión de listas
# [nueva_expresion for elemento in iterable if condicion]

# Ejemplo comprension de listas
numeros = [1, 2, 3, 4, 5, 6]
pares = [x for x in numeros if x % 2 == 0]
print(pares)

# Ejemplo elevando números al cuadrado
lista_numeros = [1, 2, 3, 4, 5, 6, 7]
cuadrado = [x**2 for x in lista_numeros]
print(cuadrado)


# Saludar a cada nombre de una lista de nombres
nombres = ['Jorge', 'Yaneth', 'Luis', 'Elena']
saludo = [f'Hola {nombre}' for nombre in nombres]
print(saludo)