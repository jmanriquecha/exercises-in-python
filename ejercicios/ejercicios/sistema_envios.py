print('Sistema de envios')

'''
Crear un programa para determinar el costo de envio de un paquete
según el destino (nacional ó internacional) y elpeso del paquete
'''

TARIFA_NACIONAL = 10 # 10 pesos * kilo
TARIFA_INTERNACIONAL = 20 # 20 pesos * kilo

costo_envio = None

# Solicita datos al cliente
destino_envio = int(input('Elija destino, 1. Nacional, 2. Internacional: '))
peso_paquete_kg = float(input('Cuál es el peso en Kg del paquete? '))

# Realizar cáculos

if destino_envio == 1:
    costo_envio = TARIFA_NACIONAL * peso_paquete_kg
else:
    costo_envio = TARIFA_INTERNACIONAL * peso_paquete_kg

print(f'Costo total del envio del paquete es ${costo_envio:.2f}')