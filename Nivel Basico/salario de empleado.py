try:
    salario = float(input("Digite el salario mensual (sin separadores): "))
    if salario > 4_000_000:
        print("Debe pagar impuesto")
        r = 0.10  # ejemplo: 10%
        impuesto = salario * r
        print(f"Impuesto aproximado ({r*100:.0f}%): ${impuesto:,.0f}")
    else:
        print("No debe pagar impuesto")
except ValueError:
    print("Entrada inválida: ingrese un número válido")