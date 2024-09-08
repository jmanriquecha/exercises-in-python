print('*** Argumentos variables **kwargs')

# *args - arguments - tupla

# **kwargs - keyword arguments (key, value) como un diccionario
def superheroe_superpoderes(nombre, *args, **kwargs):
    print('Superheroe', nombre)
    print('Tupla de valores', args)
    print('Más información', kwargs)
    
superheroe_superpoderes('Spiderman', 'Telaraña', 'vision borrosa', edad = 30, empresa='Marvel' )
superheroe_superpoderes('Iroman', edad=25)