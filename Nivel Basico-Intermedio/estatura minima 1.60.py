try:
    estatura = float(input("Ingrese la estatura (en metros): "))
    
    if estatura < 0:
        print("La estatura no puede ser negativa")
    elif estatura >= 1.60:
        print(f"Estatura {estatura} m: CUMPLE el requisito mínimo")
    else:
        print(f"Estatura {estatura} m: NO CUMPLE el requisito mínimo")
except ValueError:
    print("Entrada inválida: ingrese un número decimal")