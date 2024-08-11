"""
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión.
"""

inversion = float(input('Ingrese la cantidad de dinero a invertir: $'))
interes_anual = float(input('¿Cual es el interés anual?: %'))
cantidad_anios = float(input('Ingrese la cantidad de años : '))

rendimiento_1anio = round(inversion * (interes_anual/100+1) ** cantidad_anios, 2)

print('Total capital optenido: $', rendimiento_1anio)