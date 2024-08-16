print('*** Sistema de creación de contraseña segura ***')

password = ''

while len(password) < 6:
    password = input('Digite su nueva contraseña, minimo 6 carácteres: ')
    print('El password ingresado no es seguro. ¡Vuelve a intentar!')
else:
    print('El password ingresado es valido!')