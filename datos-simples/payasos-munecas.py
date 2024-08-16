""""
Una juguetería tiene mucho éxito en dos de sus productos: 
payasos y muñecas. Suele hacer venta por correo y la empresa 
de logística les cobra por peso de cada paquete así que deben 
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número 
de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete 
que será enviado.
"""

cantidad_payasos = int(input('Ingrese la cantidad de payasos: '))
cantidad_munecas = int(input('Ingrese la cantidad de muñecas: '))

peso_payaso = 112
peso_muneca = 75

total_peso_payasos = cantidad_payasos * peso_payaso
total_peso_munecas = cantidad_munecas * peso_muneca

peso_total_paquete = total_peso_payasos + total_peso_munecas

print(f'El peso total del paquete es de: {peso_total_paquete} g')

#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/