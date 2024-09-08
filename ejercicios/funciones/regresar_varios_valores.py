print('*** Regresar una tupla de valores desde una función ***')

# Definición de la función
def persona_mayuscula(nombre, apellido, edad):
    print(f'Esta función regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

nombre, apellido, edad = persona_mayuscula('camilo', 'reyes', 21)
print(f'Aplicando unpakin: {nombre} {apellido} {edad}')