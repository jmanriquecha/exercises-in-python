print('*** Coordenada de X, Y, Z ***')

def obtener_coordenadas(x, y, z):
    return x, y, z

resultado = obtener_coordenadas(10, 30, 20)
print(resultado)

# Aplicando Unpacking de la tupla

x1, y1, z1 = resultado
print(f'Coordenada X: {x1}, Y: {y1}, Z: {z1}')