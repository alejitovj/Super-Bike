try:
    promedio = float(input("Ingrese el promedio acumulado: "))

    if promedio < 0 or promedio > 5:
        print("Promedio no válido")
    elif promedio >= 4.5:
        print("Obtiene BECA")
    elif promedio >= 3.5:
        print("Obtiene ESTÍMULO")
    else:
        print("No obtiene ningún beneficio")
except ValueError:
    print("Ingrese un promedio válido")