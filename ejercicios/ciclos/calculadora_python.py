# Calculadora python oprear 2 números

print('*** Calculadora Python ***')

salir = False
resultado = None

while not salir:
    print('''Operaciones que puedes realizar
          1. Suma
          2. Resta
          3. Multiplicación
          4. División
          5. Salir''')
    opcion = int(input('Selecciona una opción: '))
    
    # Solicitamos información de los operandos
    if 1 <= opcion <= 4:
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
    
    # Revisamos el tipo de operación a realizar
    if opcion == 1:
        resultado = num1 + num2
        print(f'Resultado de la suma: {resultado:.2f}')
    elif opcion == 2:
        resultado = num1 - num2
        print(f'Resultado de la resta: {resultado:.2f}')
    elif opcion == 3:
        resultado = num1 * num2
        print(f'Resultado de la multiplicación: {resultado:.2f}')
    elif opcion == 4:
        resultado = num1 / num2
        print(f'Resultado de la división: {resultado:.2f}')
    elif opcion == 5:
        print('Saliendo del sistema de calduladora. Hasta pronto...')
        salir = True
    else:
        print('Opción seleccionada no es valida!')