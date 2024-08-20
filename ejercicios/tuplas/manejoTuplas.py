print('*** Manejo de tupla ***')

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)

#no podemos modificar una tupla

#mi_tupla[0] = 3

for elemento in mi_tupla:
    print(elemento, end=(' '))
    
# Crear una tupla para una coordenada en x, y  
coordenada = (3, 5)

# Accediendo a cada elemento de la tupla
print(f'\nCoordenada en el eje x: {coordenada[0]}')
print(f'Coordenada en el eje y: {coordenada[1]}')


# tupla unitaria
tupla_unitaria = 3,
print('\nTupa unitaria',tupla_unitaria)

# tupla anidada
tupla_anidada = (1, (2, 3), (4, 5))
print('\nTupla anidada', tupla_anidada[1][0])

# Tupla separada por coma
tupla_separada_coma = 3, 5, 6, 6, 3, 7, ('Otra tupla', 4)
print('\nTupla separada por coma', tupla_separada_coma)