print('*** Imprimir factorial de un número ***')
# Calcular el factorial de un número con recursividad

# factorial = 1
# for fact in range(1,5):
#     factorial *= fact
    
# print(factorial)


# factorial = 1
# def factorial_recursivo(n):
#     global factorial
#     if(n == 1):
#         factorial = 1
#     else:
#         factorial_recursivo(n - 1)
#         factorial *= n
#     return factorial
    
# # Calcular factorial de un número
# num_fact = 5
# resultado = factorial_recursivo(num_fact)
# print(f'Factorial de {num_fact}! es {resultado}')

def factorial(numero):
    # caso base
    if numero == 0 or numero == 1:
        return 1
    else:
        # caso recursivo
        fact = numero * factorial(numero - 1)
        return fact

numero = 5
resultado = factorial(numero)
print(resultado)
    