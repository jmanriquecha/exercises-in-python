print('*** Lista de suscriptores ***')

# Definimos lista de suscriptores
suscriptores = set()

# Pedimos al usuario la cantidad de suscriptores
numero_suscriptores = int(input('Ingrese la cantidad de suscriptores: '))

for _ in range(numero_suscriptores):
    suscriptores.add(input('Suscriptor (Email: )'))

# Verificamos si un nuevo suscriptor esta en la lista
nuevo_suscriptor = input('Ingresa nuevo suscriptor (Email): ')

if nuevo_suscriptor in suscriptores:
    print('El suscriptor que intentas agregar ya existe!! ')
else:
    suscriptores.add(nuevo_suscriptor)
    print('Nuevo suscriptor agregado correctamente!!')
    
# Eliminar suscriptor ya existente
eliminar_suscriptor = input('Ingresa (Email) del suscriptor a eliminar: ')

if eliminar_suscriptor in suscriptores:
    suscriptores.remove(eliminar_suscriptor)
    print(f'Suscriptor {eliminar_suscriptor} fue eliminado correctamente')
else:
    print('El suscriptor que intentas eliminar no existe!!')
    
print('\n',suscriptores)

# Verificar cantidad de suscriptores
cantidad_suscriptores = len(suscriptores)

print(f'/Cantidad de suscriptores: {cantidad_suscriptores}')

print('\n--- Listado de Suscriptores ---')

for suscriptor in suscriptores:
    print(f'- {suscriptor}')