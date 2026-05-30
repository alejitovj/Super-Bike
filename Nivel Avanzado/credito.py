try:
    valor = float(input("Ingrese el valor del préstamo: "))
    historial = input("Ingrese historial crediticio (bueno, regular, malo): ").strip().lower()

    if valor < 0:
        print("Valor no válido")
    elif historial == "bueno" and valor <= 1000000:
        print("Crédito aprobado")
    elif historial == "regular" and valor <= 500000:
        print("Crédito aprobado con condiciones")
    else:
        print("Crédito rechazado")
except ValueError:
    print("Ingrese un valor numérico para el préstamo")