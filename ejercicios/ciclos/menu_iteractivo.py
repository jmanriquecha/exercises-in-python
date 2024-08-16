print('*** Sistema de Administración de Cuentas ***')
print('Menu:')

while True:
    print(f'''
          1. Crear cuenta
          2. Eliminar cuenta
          3. Salir
          ''')
    opcion = int(input('Escoge una opción: '))
    
    if opcion == 1:
        print('Creando tú cuenta')
    elif opcion == 2:
        print('Eliminando tú cuenta')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto...')
        break
    else:
        print('Opción no valida, por favor intente nuevamente.')