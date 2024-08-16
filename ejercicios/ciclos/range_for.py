# Función range(inicio(Opcional), fin(Obligatorio), incremento(Opcional))

FIN = 5

#Imprimir los números del 1 al 5

for numero in range(1, FIN+1, 3):
    print(numero, end=(' '))
    
print('\n\nSecuencia del 10 al 20')

for numero in range(10, 20 + 1):
    print(numero, end=' ')
    
    
print('\n\nSecuencia del 20 al 30 de 2 en 2')

for i in range(20, 30 + 1, 2):
    print(i, end=' ')
