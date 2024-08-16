# Comprobar si un valor esta dentro de rango
print('*** Sistema para comprobar si un valor esta dentro de rango ***')

# Declaramos CONSTANTES
MIN = 0
MAX = 5

# Solicita datos al usuario
numero = int(input(f'Ingrese un número entero entre {MIN} y {MAX}: '))

# Realiza validaciones
# esta_en_rango = numero >= MIN and numero <= 5
esta_en_rango = MIN <= numero <= MAX

# Informa al usuario por consola
print(f'¿El número {numero} esta en el rango de {MIN} y {MAX}? {esta_en_rango}')
