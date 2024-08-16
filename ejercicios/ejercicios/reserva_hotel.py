# Sistema de reserva hotel
print('*** Bienvenido al sistema de reservas del Hotel ***')

nombre_cliente = input('Ingrese nombre del cliente: ').strip().capitalize()
dias_estancia = int(input('Cuantos dias te vas a quedar en el hotel? '))
cuarto_vista_mar = input('Quieres cuarto con vista al mar? (Sí/No) ').strip().lower()

# Tarifas Hotel
tarifa_noche = 0

usuario_quiere_vista_mar = cuarto_vista_mar == 'si'

if usuario_quiere_vista_mar:
    tarifa_noche = 190.50 # Valor diario
else:
    tarifa_noche = 150.50 # Valor diario
    
valor_total = tarifa_noche * dias_estancia

print(f'''
      ------------------------------------------------------------------------
      Detalle de la compra:
      
      Cliente: {nombre_cliente}
      Días de estancía: {dias_estancia}
      Costo total: ${valor_total:.2f}
      Habitación con vista al mar: {'Sí' if usuario_quiere_vista_mar else 'No'}
      
      ¡Gracias por preferirnos!
      ''')
