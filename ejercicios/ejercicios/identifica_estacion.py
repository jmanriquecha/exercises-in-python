print('*** Identifica la estación del año ***')

mes = int(input('Ingresa un mes del año entre 1 y 12: '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Estación desconocida'

print(f'La estación para el mes {mes} es: {estacion}')