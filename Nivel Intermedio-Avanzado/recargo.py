try:
    dias = int(input("Ingrese número de días de retraso: "))
    if dias < 0:
        print("La cantidad no puede ser negativa")
    elif dias == 0:
        print("No hay recargo")
    elif dias <= 5:
        recargo = 0.05
        print(f"Recargo aplicado: {recargo*100:.0f}%")
    elif dias <= 10:
        recargo = 0.10
        print(f"Recargo aplicado: {recargo*100:.0f}%")
    else:
        recargo = 0.20
        print(f"Recargo aplicado: {recargo*100:.0f}%")
except ValueError:
    print("Entrada inválida: ingrese un número entero")