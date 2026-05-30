try:
    tipo = input("Ingrese tipo de cliente (VIP/normal): ").strip().lower()
    compra = float(input("Ingrese valor de la compra: "))
    
    if tipo == "vip":
        descuento = 0.20
    elif tipo == "normal":
        descuento = 0.10
    else:
        descuento = 0.0
    
    total = compra * (1 - descuento)
    print(f"Descuento aplicado: {descuento*100:.0f}%")
    print(f"Total a pagar: ${total:,.2f}")
except ValueError:
    print("Entrada inválida: ingrese un número decimal")