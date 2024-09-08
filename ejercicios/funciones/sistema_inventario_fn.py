print('*** Sistema de inventarios (con funciones) ***')

inventario = [
                {'id':1, 'nombre': 'camisa', 'precio':25.99, 'cantidad':50},
                {'id':2, 'nombre':'pantalon', 'precio':256, 'cantidad':52}
             ]

# Mostrar inventario
def mostrar_inventario():
    print('--- Productos en almacén ---')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')}, Precio: ${producto.get('precio'):.2f}, Cantidad: {producto.get('cantidad'):.0f} ')

# Agregar nuevo producto
def nuevo_producto(id, nombre, precio, cantidad):
    producto = {'id':id, 'nombre':nombre, 'precio':precio, 'cantidad':cantidad}
    buscar_id = buscar_producto(id)
    if buscar_id != False:
        print(f'El producto con ID {id} ya existe!')
    else:
        inventario.append(producto)
        print('Producto agregado correctamente! ')       
        
# Buscar producto por ID
def buscar_producto(id):
    # pass
    for producto in inventario:
        if producto['id'] == id:
            print(f'ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']:.0f}')
            return
    return False
            
# Salir
def salir():
    print('Hasta luego!') 
    

if __name__ == '__main__':

    # Mostrar menu
    while True:    
        print('\n--- Menú ---')
        print(f'''
            1. Mostrar inventario
            2. Agregar producto
            3. Buscar producto por ID
            4. Salir
            ''')
        opcion = int(input('Selecciona una opción (1-4): '))
        
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            print('--- Agregar nuevo producto ---')
            id = int(input('Id: '))
            nombre = input('Nombre: ')
            precio = float(input('Precio: '))
            cantidad = int(input('Cantidad: '))
            nuevo_producto(id, nombre, precio, cantidad)
        elif opcion == 3:
            print('--- Buscar producto por ID ---')
            buscar_id = int(input('Ingresa el ID del producto a buscar: '))
            if buscar_producto(buscar_id) == False:
                print('\nProducto no encontrado\n')
        elif opcion == 4:
            salir()
            break
        else:
            print('Opción invalida, selecciona una opción válida')
        