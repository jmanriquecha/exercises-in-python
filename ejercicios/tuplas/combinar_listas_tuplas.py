print('*** Combinación de listas y tuplas ***')

lista_productos = []
lista_productos.append(('P001', 'Camisa', 20.0))
lista_productos.append(('P002', 'Jeans', 30.0))
lista_productos.append(('P003', 'Sudadera', 40.0))

print(lista_productos)

# Calculamos el precio total de los productos

precio_total = 0

for producto in lista_productos:
    #precio_total += producto[2]
    id, nombre, precio = producto #unpacking
    print(f'\nID, {id} Nombre: {nombre} Precio: ${precio:.2f}')
    precio_total += precio

print('\nPrecio total de los productos es:', f'${precio_total:.2f}')