# Descuentos por compras superiores a $200,000 #
total_compra = float(input("Ingrese el total de la compra realizada: "))
r = 0.10

if total_compra >= 200000:
    descuento = total_compra * r
    total_a_pagar = total_compra - descuento

    print(f"Señor, su compra total fue de: ${total_compra:.0f}. "
        f"Descuento aplicado {r*100:.0f}%: ${descuento:.0f}. "
        f"Total a pagar: ${total_a_pagar:.0f}.")
else:
    print(f"No aplica descuento. Total a pagar es: ${total_compra:.0f}.")