print('*** Generación de ticket de venta ***')

precio_leche = float(input('Precio de leche: '))
precio_pan = float(input('Precio de pan: '))
precio_lechuga = float(input('Precio de lechuga: '))
precio_platanos = float(input('Precio de platanos: '))
descuento = float(input('¿Aplicar descuento:? % '))

# Calculo del subtotal

subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Descuentos
valor_descuento = subtotal * (descuento / 100)

# Calcula subtotal despues de descuentos
subtotal_descuentos = subtotal - valor_descuento


# impuestos (16%)

impuesto = subtotal_descuentos * 0.16

#calculo total de la compra ( Con impuestos )
costo_total_compra = subtotal_descuentos + impuesto

print(f'''
      .............................................
        Subtotal: ${subtotal:.2f}
        Porcentaje de Descuento: {descuento:.0f}%
        Total descuento: ${valor_descuento:.2f}
        Subtotal despues de descuentos: {subtotal_descuentos:.2f}
        Impuestos (16%): ${impuesto:.2f}
        Total Compra: ${costo_total_compra:.2f}
      .............................................
      ''')