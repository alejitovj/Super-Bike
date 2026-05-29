try:
    temp = float(input("Ingrese la temperatura de la ciudad (°C): "))
    if temp <= 10:
        print("Clima: Frío")
    elif temp <= 25:
        print("Clima: Templado")
    else:
        print("Clima: Caliente")
except ValueError:
    print("Entrada inválida: por favor ingrese un número.")