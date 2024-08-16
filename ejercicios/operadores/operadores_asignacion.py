# Operadores de asignación

# variable = valor

# Asignacion multiple

a, b, c = 10, 'Saludo', 25.4

print(a,b,c)

## Asignación encadenada

variable1 = variable2 = 0
print(f'Variable 1 {variable1} variable 2 {variable2}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'X: {x}, Y: {y}')

# Aplicando el concepto de asignación multiple, intercambiamos las variables
x, y = y, x
print(f'X: {x}, Y: {y}')

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tús nombres y apellidos separados por coma(,): ').split(',')
print(f'Hola, {nombre.strip()} tús apellidos son {apellido.strip()}')
