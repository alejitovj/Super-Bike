try:
    peso = float(input("Ingrese el peso del paquete (kg): "))
    
    if peso < 0:
        print("El peso no puede ser negativo")
    elif peso <= 1:
        costo = 5000
        print(f"Peso: {peso} kg - Costo: ${costo:,.0f}")
    elif peso <= 5:
        costo = 10000
        print(f"Peso: {peso} kg - Costo: ${costo:,.0f}")
    elif peso <= 10:
        costo = 15000
        print(f"Peso: {peso} kg - Costo: ${costo:,.0f}")
    else:
        costo = 20000
        print(f"Peso: {peso} kg - Costo: ${costo:,.0f}")
except ValueError:
    print("Entrada inválida: ingrese un número decimal")