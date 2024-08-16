##Generador de email

print('*** Generador de Emails ***')

nombre = '        Jorge Manrique Chavarro '
empresa = 'Global Mentoring'
dominio = '           com.co'

## Convertir texto a minusculas y quita espacios al inicio y al final en blanco
nombre = nombre.lower().strip()
empresa = empresa.lower().strip()
dominio = dominio.lower().strip()

## Da formato al texto

#Remplaza espacios en el nombre por .
nombre = nombre.replace(' ', '.')

#Quita los espacios en la empresa
empresa = empresa.replace(' ', '')

## Genera correo electronico 
extencion_dominio = f'.{dominio}'
dominio = f'@{empresa}{extencion_dominio}'

genera_email = f'{nombre}{dominio}'
print(f'Email generado: {genera_email}')

# ## Ver resultados
# imprimir_datos = f"""
# Nombre: {nombre} 
# Empresa: {empresa} 
# Dominio: {dominio}
# """
# print(imprimir_datos)