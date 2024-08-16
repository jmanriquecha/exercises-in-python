# Declaración de variables
nombre = input('Ingrese el nombre del Cliente ')
dias_estancia = int(input('Días de Estancia '))
tarifa_diaria = float(input('Ingrese el valor de la tarifa diaria '))
vista_mar = input('¿La habitación cuenta con vista al mar? ')

print("*** Sistema de Reserva de Hoteles ***")
print(f'Cliente: {nombre}')
print(f'Días de estancia: {dias_estancia}')
print(f'Tarifa diaria: {tarifa_diaria}')
print(f'¿Habitación con vista al mar?: {True if int(vista_mar) == 1 else False}')
