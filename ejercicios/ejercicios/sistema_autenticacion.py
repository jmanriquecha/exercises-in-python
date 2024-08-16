#Sistema de autenticación

print('*** Sistema de autenticación de usuarios ***')

# Definimos constantes
USER = 'jorge123'
PASS = 'Pass123'

# Solicitamos información al usuario
usuario = input('Ingrese el nombre de usuario: ')
contrasena = input('Ingrese la contraseña: ')

# Comparamos los valore proporcionados por el usuario con las CONSTANTES
es_usuario = usuario.strip() == USER
es_contrasena = contrasena.strip() == PASS

# Realizamos validaciones para que los dos sean True
usuario_autenticado_ok = es_usuario and es_contrasena

# Mostramos información por consola
print(f'Estado de autenticación es: {usuario_autenticado_ok}')