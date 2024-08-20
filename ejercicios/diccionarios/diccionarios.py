print('*** Diccionarios en python ***')

# Definimos el diccionario
persona = {'nombre': 'petito',
           'apellido': 'perez',
           'pais':'Colombia',
           'edad':20,
           'es_casado' : True
           }

# Imprimir diccionario
print(f'\nDiccionario persona: {persona}')

# acceder a las llaves o claves
# Acceder a la edad de la persona
edad_persona = persona['edad']
print(f'Edad de la persona: {edad_persona}')

# Acceder sí es casado ó  no
si_es_casado = persona.get('es_casado')
print(f'Obtenemos sí es casado: {si_es_casado}')

# Imprimir pais
print(f'Pais: {persona["pais"]}')
# print(f'Pais: {persona.get('pais')}')


# modificar un diccionario
persona['pais'] = 'Nicaragua'

print('\nPersona modificada', persona)

# Agregar nuevo elementos a un diccionario
persona['sexo'] = 'Masculino'

print('\nDiccionario Actualizado', persona)

# Eliminar elemento de un diccionario
del persona['pais']
print('\nDiccionario Actualizado', persona)


persona.pop('sexo')
print('\nDiccionario Actualizado', persona)

# Iterar los elementos de un diccionario
for llave, valor in persona.items():
    print(f'LLave: {llave}, Valor: {valor}')
    
# Obtener solo los valores
for valor in persona.values():
    print(f'Valor: {valor}')
    
# Obtener solo las llaves keys
for key in persona.keys():
    print(f'LLaves {key}')