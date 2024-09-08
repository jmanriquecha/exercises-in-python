print('*** Imprimir detalles de una persona **kwargs ***')

# Funcion que acepta argumentos variables {llave:valor} diccionario
def imprimir_detalle_persona(**kwargs):
    print('Valores recibios: ')
    # for detalle in kwargs:
    for key, detalle in kwargs.items():
        print(key, detalle)
        

# Ejecuta funcion
imprimir_detalle_persona(nombre='Jorge', apellido='Manrqiue', edad=30, sexo='M')