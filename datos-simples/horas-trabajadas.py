#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = float(input('Ingrese el número de horas trabajadas: '))
valor_hora = float(input('Digite el valor de cada hora: $ '))

result = horas_trabajadas * valor_hora

print(f'Valor total correspondiente: ${result}')