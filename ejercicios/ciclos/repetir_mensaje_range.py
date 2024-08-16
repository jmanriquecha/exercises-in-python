# Impresión de mensaje
print('*** Repetición de mensaje ***')

mensaje = input('Proporciona un mensaje a repetir: ')
num_repeticiones = int(input('Ingresa número de repeticiones: '))

for _ in range(num_repeticiones): # Sí no se utiliza la variable en el for se sule colocar _
    print(mensaje)