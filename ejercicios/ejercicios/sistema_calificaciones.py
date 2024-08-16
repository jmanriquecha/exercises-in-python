print('*** Bienvenido al sistema automatico de calificaciones ***')

califiacion = float(input('Ingrese la calificación del estudiante entre (0 y 10): '))

letra = None

# Validaciones
if 9 <= califiacion <= 10:
    letra = 'A'
elif 8 <= califiacion < 9:
    letra = 'B'
elif 7 <= califiacion < 8:
    letra = 'C'
elif 6 <= califiacion < 7:
    letra = 'D'
elif 0 <= califiacion < 6:
    letra = 'F'
else:
    letra = 'Valor desconocido'

    
print(f'La calificación de {califiacion:.1f} corresponde a letra: {letra}')