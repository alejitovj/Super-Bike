try:
    faltas = int(input("Ingrese el número de faltas: "))
    if faltas < 0:
        print("Número no válido")
    elif faltas == 0:
        print("Excelente asistencia")
    elif faltas <= 3:
        print("Asistencia aceptable")
    elif faltas <= 6:
        print("Riesgo académico")
    else:
        print("Estado académico en peligro")
except ValueError:
    print("Entrada inválida: ingrese un número entero")