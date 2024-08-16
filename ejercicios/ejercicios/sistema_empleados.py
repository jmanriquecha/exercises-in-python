# Sistema de registro de empleados

print('*** Sistema de registro de empleados ***')

nombre_empleado = input('Ingrese el nombre del empleado: ')
edad_empleado = int(input('Ingrese la edad del empleado: '))
salario_empleado = float(input('Ingrese el salario del empleado: '))
es_jefe_departamento = input('Ingrese (Sí/No) es jefe de departamento: ').lower()

es_jefe_departamento = es_jefe_departamento == 'si' or es_jefe_departamento == 'sí'

print(f'Nombre de Empleado: {nombre_empleado}')
print(f'Edad de Empleado: {edad_empleado}')
print(f'Salario de Empleado: {salario_empleado:.2f}')
print(f'Empleado es jefe de departamento: {es_jefe_departamento}')