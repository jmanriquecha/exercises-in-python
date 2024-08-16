#Casa de los espejos aplicando logica inversa

print('Bienvenidos a la casa de los espejos: ')

edad = int(input('Ingrese su edad: '))
tiene_miedo = input('Tienes miedo a la oscuridad? (Sí/No) ')

edad_ok = edad >= 10
miedo_oscuridad = tiene_miedo.strip().lower() == 'si'

if edad_ok and not miedo_oscuridad:
    print('Puedes entrar a la casa de los espejos: ')
else:
    print('No puedes entrar a la casa de los espejos ')