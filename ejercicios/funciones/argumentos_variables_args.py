print('*** Argumentos posicionales variables ***')

# *args - arguments - tupla
# Argumentos variables y los recibe en tupla
# *args es lo recomendado por python
def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} = {args}')
    
# Llamar función
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Telaraña')