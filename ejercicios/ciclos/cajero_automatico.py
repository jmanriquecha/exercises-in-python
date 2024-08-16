print('*** Aplicación de cajero automatico ***')

saldo_actual = 1000
salir = False

while not salir:
    print('''
          Operaciones que puedes realizar:
            1. Consultar saldo
            2. Retirar
            3. Depositar
            4. Salir
          ''')
    opcion = int(input('Escoje una opción: '))
    
    if opcion == 1:
        print(f'Su saldo actual es: ${saldo_actual:.2f}')
    elif opcion == 2:
        retiro = float(input('Ingresa el monto a retirar: '))
        if retiro > saldo_actual:
            print(f'No cuentas con el saldo suficiente. Saldo actual ${saldo_actual:.2f}')
        else:
            saldo_actual -= retiro
            print(f'Tu nuevo saldo es ${saldo_actual:.2f}')
    elif opcion == 3:
        deposito = float(input('Ingrese el dinero a depositar: '))
        saldo_actual += deposito
        print(f'Tú nuevo saldo es : ${saldo_actual:.2f}')
    elif opcion == 4:
        print('Saliendo del sistema, hasta pronto...')
        salir = True
    else:
        print('Opción incorrecta!')
else:
    print('Finalizando while')