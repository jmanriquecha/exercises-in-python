print('*** Operaciones con Sets ó Conjuntos ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unir dos sets o conjuntos
union = a | b
print(f'\nUnión de a y b {union}')

# Intercección de dos conjutos Sets
interseccion = a & b
print(f'\nIntesección de dos conjuntos Sets {interseccion}')

# Diferencia  de dos conjuntos A-B, es el conjunto de elementos que estan en A pero no en B
diferencia_a = a - b
print(f'\nElmentos que estan en A pero no en B {diferencia_a}')

# Diferencia  de dos conjuntos B-A, es el conjunto de elementos que estan en B pero no en A
diferencia_b = b - a
print(f'\nElmentos que estan en B pero no en A {diferencia_b}')

# Diferencia simetrica de dos conjuntos Sets, es el conjunto de elementos que estan en A ó B pero no en ambos
diferencia = a ^ b
print(f'\nDiferencia de los conjuntos Sets: {diferencia}')
