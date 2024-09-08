print('*** Diccionario combinado con listas ***')

# Creando diccionario
personas = [    
    {
        'nombre': 'Regina',
        'apellido': 'Flores',
        'edad': 21
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 32
    }        
    ]

# Imprimir todos los contactos
print('Imprime personas', personas)


# Acceder a Regina
print(personas[0].get('nombre'))

print('\nIterar sobre todos los contactos')
# Iterar 
for persona in personas:
    print(f'''
          Nombre: {persona.get('nombre')}
          Apellido: {persona.get('apellido')}
          Edad: {persona.get('edad')}''')
    
# Imprimir diccionario personas
for contador, persona in enumerate(personas):
    print(f'{contador} - {persona}')