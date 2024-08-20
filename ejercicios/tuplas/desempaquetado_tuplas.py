print('*** Desempaquetando tuplas ***') # unpacking

producto = ('P001', 'Camisa', 20.00)

# Desempaquetado
id, descripcion, precio = producto
print('Tupla producto completa:',producto)

#Tupla desempaquetada
print(f'\nTupla desempaquetada -> ID: {id}, Descripción: {descripcion}, Precio: ${precio}')
