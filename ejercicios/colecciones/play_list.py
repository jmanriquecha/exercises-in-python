# Play List
print('*** Playlist ***')

# Crear Play List
playlist = []

agregar_canciones = int(input('¿Cuántas canciones deseas agregar al Playlist? '))
contador = 0

while contador < agregar_canciones:
    nueva_cancion = input(f'Nombre de la canción {contador + 1}: ')
    playlist.append(nueva_cancion)
    contador += 1

# Muestra listado de canciones agregadas
print('-----------------------------------')
print(f'Lista de reproducción: ')
print('___________________________________')

# Ordenar lista de reproducción por orden alfábetico
playlist.sort()
#playlist.sort(reverse=True)

for i in range(len(playlist)):
    print(f'{i + 1}. {playlist[i]}')
