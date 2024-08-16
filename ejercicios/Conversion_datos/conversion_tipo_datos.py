#Conversion de datos (casting)

#Convertir cadena a número
numero_cadena = '10'
numero_entero = int(numero_cadena)

print(type(numero_entero))

# Convertir cadena a flotante
pi_cadena = '3.1416'
pi_flotante = float(pi_cadena)

print(type(pi_flotante))

## Convertir de numero a cadena
numero = 3
numero_a_texto = str(numero)
print(numero_a_texto)

# Convertir a bool
# Tipo bool es False en los siguientes casos
# Si es cero 0, None, entonces regresa False
# Regresa True, si el valor es distinto de 0, si es distinto de cadena vacia 
# y tambien si es distinto de None = "Ausencia de valor"

numero_entero1 = None
booleano = bool(numero_entero1)

print(booleano)