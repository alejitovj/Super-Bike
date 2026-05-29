try:
    materias_perdidas = int(input("Ingrese la cantidad de materias perdidas: "))
    
    if materias_perdidas < 0:
        print("La cantidad no puede ser negativa")
    elif materias_perdidas >= 2:
        print("El aprendiz entra en PLAN DE MEJORAMIENTO")
    else:
        print("El aprendiz no entra en plan de mejoramiento")
except ValueError:
    print("Entrada inválida: ingrese un número entero válido")