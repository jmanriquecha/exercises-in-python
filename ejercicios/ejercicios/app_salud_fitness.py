# App salud y fitness
print('*** Bienvenido al sistema de salud y fitness ***')

nombre_usuario = input('Ingrese el nombre de usuario: ').strip().capitalize()
pasos_caminados_dia = int(input('Ingese pasos caminados durante el día: '))

META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

# Calculamos calorias quemadas

calorias_quemadas = pasos_caminados_dia * CALORIAS_POR_PASO

# Meta alcanzada
meta_alcanzada = pasos_caminados_dia >= META_PASOS_DIARIOS

print(f'''
      Hola, {nombre_usuario},
      Resumen de tú día:
        Meta de pasos diarios: {META_PASOS_DIARIOS} pasos
        Pasos caminados hoy: {pasos_caminados_dia}
        Calorias quemadas: {calorias_quemadas:.0f} kcal
        {'Felicidades! Alcanzaste la meta de pasos diarios' if meta_alcanzada else 'No haz alcanzado la meta de pasos diarios' }
      ''')