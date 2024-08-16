# Promediar n calificaciones
print('*** Sistema de promedio de califiaciones ***')

numero_calificaciones = int(input('Ingrese el número de calificaciones a promediar: '))
list_notas = []
acumulado = 0
cont = 0


while cont < numero_calificaciones:
    nota = float(input(f'Ingrese la nota {cont + 1}: '))
    list_notas.append(nota)
    acumulado += nota
    cont += 1
    
# Promediar notas
promedio = acumulado / len(list_notas)

print(f'El promedio obtenido es: {promedio:.1f}')