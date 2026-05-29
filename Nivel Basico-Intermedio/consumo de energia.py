try:
    consumo = float(input("Ingrese el consumo de energía (kWh): "))
    
    if consumo < 0:
        print("El consumo no puede ser negativo")
    elif consumo <= 100:
        print(f"Consumo {consumo} kWh: BAJO")
    elif consumo <= 300:
        print(f"Consumo {consumo} kWh: MEDIO")
    else:
        print(f"Consumo {consumo} kWh: ALTO")
except ValueError:
    print("Entrada inválida: ingrese un número decimal")