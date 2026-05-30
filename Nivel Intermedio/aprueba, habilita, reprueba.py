try:
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    
    promedio = (nota1 + nota2 + nota3) / 3
    
    if promedio >= 3.0:
        print(f"Promedio: {promedio:.1f} - APRUEBA")
    elif promedio >= 2.0:
        print(f"Promedio: {promedio:.1f} - HABILITA")
    else:
        print(f"Promedio: {promedio:.1f} - REPRUEBA")
except ValueError:
    print("Entrada inválida: ingrese números decimales")