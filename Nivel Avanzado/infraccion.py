try:
    velocidad = float(input("Ingrese la velocidad del vehículo (km/h): "))
    if velocidad < 0:
        print("Velocidad no válida")
    elif velocidad <= 60:
        print("No hay infracción")
    elif velocidad <= 80:
        print("Infracción leve")
    elif velocidad <= 100:
        print("Infracción grave")
    else:
        print("Infracción muy grave")
except ValueError:
    print("Ingrese una velocidad válida")