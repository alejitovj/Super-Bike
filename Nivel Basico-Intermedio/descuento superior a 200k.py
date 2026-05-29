try:
    compra = float(input("Ingrese el valor de la compra ($): "))
    
    if compra < 0:
        print("El valor no puede ser negativo")
    elif compra > 200000:
        descuento_porcentaje = 10
        descuento = compra * (descuento_porcentaje / 100)
        total_pagar = compra - descuento
        
        print(f"Compra original: ${compra:,.0f}")
        print(f"Descuento ({descuento_porcentaje}%): ${descuento:,.0f}")
        print(f"Total a pagar: ${total_pagar:,.0f}")
    else:
        print(f"Compra: ${compra:,.0f}")
        print("No aplica descuento")
except ValueError:
    print("Entrada inválida: ingrese un número decimal")