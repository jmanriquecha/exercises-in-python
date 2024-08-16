from random import randint

# Sistema generador de ID unico
print('*** Sistema Generador de ID único ***')

nombre = input('Ingrese nombre: ').strip()
apellido = input('Ingrese apellido: ').strip()
anio_nacimiento = input('Ingrese año de nacimiento (YYYY): ').strip()

# 1 Del valor recibido de nombre, usar sólo las 2 primeras letras y convertirlas a mayúsculas
nombre_modificado = nombre[0:2].upper()
# print(nombre)

# 2 Del valor de apellido, usar sólo las 2 primeras letras y convertirlas a mayúsculas
apellido_modificado = apellido[0:2].upper()
# print(apellido)

# 3 De año sólo vamos a tomar los 2 últimos digitos
anio_nacimiento_modificado = anio_nacimiento[2:]
# print(anio_nacimiento)

# 4 Es sistema deberá generar un valor aleatorio de  digitos, con ayuda de la función randint
min = 1000
max = 9999
aleatorio = randint(min,max)
# print(aleatorio)

# Resultado ID único

id_unico = f'{nombre_modificado}{apellido_modificado}{anio_nacimiento_modificado}{aleatorio}'

print(f"""
      ----------------------------------------------------------------------
      Hola, {nombre.capitalize()}
        El nuevo número de identificación (ID) generado por el sistema es:
        {id_unico}
        Felicidades!
      """)