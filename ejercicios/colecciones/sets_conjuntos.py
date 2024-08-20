print('*** sets en python ***')

# Set o conjuntos {}

mi_set = {1, 2 ,3 ,4, 5, 4}
print(mi_set)

## Agregar elementos a un set
mi_set.add(6)
mi_set.add(7)

print(mi_set)

## Intentando agregar un elemento duplicado
mi_set.add(5)
mi_set.add('jajaja')
print(mi_set)


## Eliminar un elemento
mi_set.remove('jajaja')
print(mi_set)

## iterar elementos
for item in mi_set:
    print(item, end=' ')
    
## comprobar si existe un elemento dentro del set

print(f'\nExiste el valor de 4 dentro del set? {4 in mi_set}')

# Obtener longitud de un set
print(f'\nLongitud del set: {len(mi_set)}')