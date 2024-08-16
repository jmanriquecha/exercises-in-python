# Nueva version de generador de emails

print('### Sistema Generador de Emails ###')

# Se debe solicitar los siguientes datos
nombres = input('Digite los nombres: ')
apellidos = input('Digite los apellidos: ')
nombre_empresa = input('Digite el nombre de la empresa: ')
extension_dominio = '.com.mx'

# Normalizar datos
nombres = nombres.strip().replace(' ', '.').lower()
apellidos = apellidos.strip().replace(' ', '.').lower()
nombre_empresa = nombre_empresa.replace(' ', '').lower()
dominio_normalizado = f'@{nombre_empresa}{extension_dominio}'

email_generado = f'{nombres}.{apellidos}{dominio_normalizado}'

# Mostrar resultado
print(f'''
      -----------------------------
      Genial! El sistema ha generado tú nuevo email :)
      
      {email_generado}
      ''')