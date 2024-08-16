# Receta de cocina
print('*** Receta de cocina ***')

nombre_receta = input('Nombre de la receta: ')
ingredientes_receta = input('Ingredientes de la receta: ')
tiempo_preparacion = int(input('Tiempo de preparación (en minutos): '))
dificultad_receta = input('¿Cual es la dificultad de la receta: (Fácil, Media, Alta) ').lower()

print('-------------------------------------------------------------')
print(f'Nombre de la receta: {nombre_receta}')
print(f'Ingredientes de la receta: {ingredientes_receta}')
print(f'Tiempo de preparación de la receta: {tiempo_preparacion} minutos')
print(f'Dificultad de la preparación de la receta: {dificultad_receta}')