print('*** Bienvenido al sistema de autenticación ***')

USUARIO_VALIDO = 'admin'
CONTRASENA_VALIDA = '123'

# Solicita datos de login al usuario
usuario = input('Ingrese el nombre de usuario: ').strip()
contrasena = input('Ingrese la contrasena: ').strip()

if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
    print('Bienvenido al sistema')
elif usuario == USUARIO_VALIDO:
    print('La contraseña no es valida')
elif contrasena == CONTRASENA_VALIDA:
    print('El usuario no es valido')
else:
    print('Usuario y contraseña invalidos')