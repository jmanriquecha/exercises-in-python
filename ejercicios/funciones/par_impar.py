print('*** Saber si un número es par ó impar ***')

# Definir función
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
        

# Ejecuta función
if __name__ == '__main__':
    
    numero = int(input('Ingrese un número para saber si es PAR: '))

    if(es_par(numero)):
        print('El número es par')
    else:
        print('El número es Impar')
