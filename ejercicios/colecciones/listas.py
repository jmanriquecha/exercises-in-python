# Sintaxis listas
# mi_lista = [1, 3, 5, 6]

print('*** Manejo de listas ***')

# Mi lista

mi_lista = [1, 'Hola Mudo', [False, None], True]

# largo de la lista
largo_lista = len(mi_lista)
print(largo_lista)

# acceder un indice de la lista
print(mi_lista[1])

# Acceder al último indice de la lista
print(mi_lista[-1])

# Modificar elementos de una lista
mi_lista[0] = 10
print(mi_lista)

# Agregar nuevo elementos
mi_lista.append(['tres', 'cuatro'])
print(mi_lista)

# Agregar nuevo elemnto en un indice especifico
mi_lista.insert(2,'quince')
print(mi_lista)


# Eliminar elementos de una lista
# por valor
mi_lista.remove('quince')
print(mi_lista)

# por indice
mi_lista.pop(2)
print(mi_lista)

# con del
del mi_lista[3]
print(mi_lista)


# Obtener sublistas
sublista = mi_lista[0:1+1]
print(sublista)