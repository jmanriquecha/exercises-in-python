# Calcula área y perímetro de un Rectángulo

print('*** Cálcula área y perímetro de un Rectángulo ***')

# Solicita datos al usuario
base = float(input('Ingrese la base del Rectángulo: '))
altura = float(input('Ingrese la altura del Rectángulo: '))

# Realiza cálculos
area = base * altura
perimetro = 2 * (base + altura)

print(f'''
      El área es: {area:.2f}
      El perímetro es: {perimetro:.2f}
      ''')