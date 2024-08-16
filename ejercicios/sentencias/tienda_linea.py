# Crear sistema que ofrezca descuentos dependiendo de monnto de la compra, o si es miembro de la tienda

valor_compra = float(input('Ingrese el valor de la compra: $'))
es_miembro = input('¿Es miembro de la tienda? (SI/NO)')

VALOR_MINIMO = 1000
es_miembro = es_miembro.strip().lower() == 'si'
descuento = 0
total_descuento = 0
total_pagar = valor_compra

if valor_compra >= VALOR_MINIMO and es_miembro:
    descuento = 0.1 # 10%
elif es_miembro:
    descuento = 0.05 #5%
elif valor_compra >= VALOR_MINIMO:
    descuento = 0.03
else:
    descuento = 0
    
total_descuento = valor_compra * descuento
total_pagar = valor_compra - total_descuento

if descuento != 0:   
    print(f'''
        --------------------------------------------------------------------------
        Felicidades! has obtenido un descuento del {descuento * 100:.0f}%
        --------------------------------------------------------------------------
        
        Sub. Valor: {valor_compra:.2f}
        Te ahorraste: ${total_descuento:.2f}
        Total Compra: ${total_pagar:.2f}
        ''')
else:
    print(f'''
        --------------------------------------------------------------------------
        Te invitamos a obtener los mejores descuentos, suscribete a nuestra empresa
        --------------------------------------------------------------------------
        
        Total Compra: ${total_pagar:.2f}
        ''')
    