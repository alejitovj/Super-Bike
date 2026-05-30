try:
    consumo = float(input("Ingrese el consumo de agua mensual en litros: "))
    if consumo < 0:
        print("Consumo no puede ser negativo")
    elif consumo <= 10000:
        print("Consumo: AHORRO")
    elif consumo <= 20000:
        print("Consumo: MODERADO")
    else:
        print("Consumo: EXCESIVO")
except ValueError:
    print("Ingrese un número válido")