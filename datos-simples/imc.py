""""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
es el índice de masa corporal calculado redondeado con dos decimales.
"""

estatura = float(input('Ingrese su estatura en metros: '))
peso = float(input('Ingrese su peso en Kg: '))

imc = (peso)/(estatura) ** 2

print('Tu IMC es:', round(imc, 2))