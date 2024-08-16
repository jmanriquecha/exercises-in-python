#Juego de adivinanzas
print('*** Juego de adivinanzad (Número Secreto) ***')

from random import randint

# Declaración de constantes y variables
MIN = 1
MAX = 50
MAX_INTENTOS = 3
intentos = 0
numero_secreto = randint(MIN, MAX)
numero_usuario = None

while numero_usuario != numero_secreto and intentos < MAX_INTENTOS:
    numero_usuario = int(input(f'Ingrese un número entre {MIN} y {MAX} '))
    if numero_usuario > numero_secreto:
        print('¡Sigue intentando! el número secreto es Menor.')
    else:
        print('¡Sigue intentando! el número secreto es Mayor.')
    intentos += 1
else:
    if numero_secreto == numero_usuario:
        print(f'¡Genial Adivinaste, el número secreto es {numero_secreto}')
        print(f'Necesitaste de {intentos} intentos.')
    else:
        print(f'Lo siento agotaste los {intentos} intentos permitidos!')
        print(f'El número secreto era: {numero_secreto}')
