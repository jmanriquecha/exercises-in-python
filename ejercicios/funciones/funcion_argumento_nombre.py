print('*** Funcion con argumentos por nombre ***')

def imprimir_persona(nombre, apellido, edad):
    print(f'Persona: nombre: {nombre}, apellido: {apellido}, edad: {edad}')
    
# Primero llamamos la función pasando los argumentos de manera posicional
imprimir_persona('Ricardo', 'Vargas', 30)

# Llamar la función usando argumentos por nombre
imprimir_persona(nombre='Sandra', apellido='Rodriguez', edad=21)
imprimir_persona(edad=55, apellido='Perez', nombre='Carlos')

# Argumentos de funciones de valores por default

def persona(nombre, apellido, edad, casado = False):
    print(f'Hola, {nombre} {apellido} tienes {edad} años y {'eres casad@' if casado else 'no eres casad@'}')
    
# ejecuta función
persona('Gabrielina', 'Rojas', 20, True)
persona('Miguel', 'Vergara', 26)