# Calcular la potencia de un número usando funciones recursivas
print('*** Calcula la potencia de un número utilizando funciones recursivas ***')

# Definir la función recursiva
def potencia_recursiva(numero, potencia):
    if potencia == 0: # Caso base
        return 1
    else:# Recursivo
        return numero * potencia_recursiva(numero, potencia - 1)

numero = 4
potencia = 5
resultado = potencia_recursiva(numero, potencia)
print(f'Resultado de elevar {numero} ^ {potencia} es {resultado}')
