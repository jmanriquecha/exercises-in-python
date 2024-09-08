print('*** Tienda de Snacks Online ***')

productos = [
    {'id': '1', 'name': 'Papas', 'precio': 30},
    {'id': '2', 'name': 'Refresco', 'precio': 50},
    {'id': '3', 'name': 'Sandwich', 'precio': 120},
    
]
productos_comprados = []

def mostrar_snacks(productos):
    print('--- Snacks Disponibles ---')
    for product in productos:
        print(f'Id: {product.get('id')} -> Nombre: {product.get('name')} - ${product.get('precio')}')

def comprar_snack():
    id_snack = int(input('Ingrese el ID del Snack a comprar: '))
    
    # Verificamos que el producto exista
    producto_encontrado = buscar_snack(id_snack)
    if producto_encontrado:     
        # Crea lista con los productos comprados
        print('Snack Agregado:', producto_encontrado)
        productos_comprados.append(producto_encontrado)
    else:
        print(f'El producto con ID {id_snack} no existe: ')
    pass

def mostrar_tickets():
    ticket = f'\t--- Ticket de venta ---'
    suma = 0
    for product in productos_comprados:
        suma += product.get('precio')
        ticket += f'\n\t- {product.get('name')} - ${product.get('precio'):.2f}'
    ticket += f'\n\tTotal -> ${suma:.2f}'
    print(ticket)

def buscar_snack(id):
    for product in productos:
        if id == int(product.get('id')):
            return product
    return False
        

if __name__ == '__main__':
    
    while True:
        print('\nMenú')
        print('''        1. Mostrar Snacks
        2. Comprar Snacks
        3. Mostrar Ticket
        4. Salir
              ''')
        option = int(input('Escoja una opción entre (1-4): '))
        
        if option == 1:
            mostrar_snacks(productos)
        elif option == 2:
            comprar_snack()
        elif option == 3:
            mostrar_tickets()
        elif option == 4:
            print('Saliendo del sistema, ¡Hasta pronto!')
            break
        else:
            print('La opción seleccionada no es válida, escoja entre (1-4)')
        
