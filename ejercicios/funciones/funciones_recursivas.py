print('*** Imprimir del 1 al 5 de forma recursiva ***')

## definimos la función
def imprimir_numeros(numero):
    #Caso base
    if numero == 1:
        print(numero, end=' ')
    else: # Caso recusiva
        imprimir_numeros(numero - 1)
        print(numero, end = ' ')

imprimir_numeros(5)