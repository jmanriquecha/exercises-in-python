print('*** break y continue ***')

print('Ejemplo break')
# Ejemplo de break
for numero in range(1, 9):
    if numero % 2 == 0:
        print(numero, end=', ')
        break # Salimos del bloque

print('\nEjemplo continue')

# Ejemplo con continue
for numero in range(1, 9):
    if numero % 2 == 0:
        print(numero, end=', ')
    else:
        continue    