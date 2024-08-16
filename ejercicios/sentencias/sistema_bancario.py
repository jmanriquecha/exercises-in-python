#Sistema bancario

#Considerando que estamos dentro de un sistema bancario, se solicita
#preguntar al usuario si desea continuar dentro del sistema

'''
    Utilizando el operador not para aplicar una lógica inversa se debe programar las 
    siguientes condiciones
    
    Si NO deseamos salir del sistema, imprimir:
        Continuamos dentro del sistema
    
    De lo contrario, imprimimos
        saliendo del sistema 
'''

continuar_en_sistema = input('Desea continuar dentro del sistema? ').strip().lower()

if not continuar_en_sistema == 'si':
    print('Continuamos dentro del sistema')
else:
    print('Salimos del sistema')
