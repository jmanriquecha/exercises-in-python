# Mayor de dos números

print('Programa para calcular cual es el número mayor ')

numero1 = int(input('Ingrese el primer número. '))
numero2 = int(input('Ingrese el segundo número. '))

es_mayor = f'El primer número es mayor: {numero1}' if numero1 > numero2 else f'El segundo número es mayor: {numero2}'

print(es_mayor)