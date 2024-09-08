print('*** Suma con argumentos variables *args ***')

# Definir la función
def suma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Ejecuta función suma
suma1 = suma(10,3,5)
print(suma1)