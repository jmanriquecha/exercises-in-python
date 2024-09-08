print('*** Gestión de Inventario ***')

cantidad_productos_add = int(input('Cuántos productos desea agregar al inventario? '))
inventario = []
contador = 0

while contador < cantidad_productos_add:
    print(f'Porporciona los valores del producto {contador + 1}')
    nombre_producto = input('Nombre: ')
    precio_producto = input('Precio: ')
    cantidad_producto = input('Cantidad: ')
    
    # Crea diccionario de cada producto
    producto = {
        'id': f'P00{contador + 1}',
        'nombre': nombre_producto,
        'precio': precio_producto,
        'cantidad': cantidad_producto
    }
    
    # Agrega producto a la lista
    inventario.append(producto)
    contador += 1

# Imprime productos
print(inventario)

# Buscar producto por ID
id_buscar = input('Ingresa el ID del producto a buscar: ')
producto_encontrado = None

for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break
    
if producto_encontrado is not None:
    print('Información del producto encontrado')
    print(f'''
          Id: {producto_encontrado.get('id')}
            Nombre: {producto_encontrado.get('nombre')}
            Precio: {producto_encontrado.get('precio')}
            Cantidad: {producto_encontrado.get('cantidad')}''')
else:
    print(f'Producto con ID {id_buscar} no encontrado')


# Muestra el inventario detallado actualizado
print('\n---Inventario detallado actualizado ---')
for producto in inventario:
    print(f'''
          Id: {producto.get('id')}
            Nombre: {producto.get('nombre')}
            Precio: {producto.get('precio')}
            Cantidad: {producto.get('cantidad')}''')