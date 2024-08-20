print('*** Agenda de contactos ***')

# definimos el diccionario
agenda = {
    'carlos':{
        'telefono':'3214564345',
        'email':'carlos@mail.com',
        'direccion': 'calle 5 #aquí'
    }
}

print(agenda)


# Acceder a un contacto en especifico
print(f'''Información de Carlos:
        Teléfono: {agenda["carlos"]['telefono']},      
        Email: {agenda["carlos"]['email']},      
        Dirección: {agenda.get('carlos').get('direccion')}      
      ''')

# Agregamos nuevo contacto
agenda['jorge'] = {'telefono':'3255489454',
                      'email':'jorge@mail.com',
                      'direccion':'calle 123 # parriba'
                      }

# Consultar agenda
print(agenda)


# Eliminar un contacto existente
# agenda.pop('carlos')
del agenda['carlos']['telefono']
print('Despues de eliminar',agenda)


# Mostrar todos los contactos de la agenda
print('\nContactos en la agenda')
for nombre, detalles in agenda.items():
    print(f'''
          ------------------------------------------
            Nombre: {nombre.capitalize()}          
          ------------------------------------------
            - Teléfono: {detalles.get('telefono')} 
            - Email: {detalles.get('email')} 
            - Dirección: {detalles.get('direccion')}''')
    