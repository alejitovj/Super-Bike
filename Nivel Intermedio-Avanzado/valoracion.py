try:
    cal = int(input("Ingrese calificación de servicio (1-5): "))
    if cal == 1:
        print("Lo sentimos, trabajaremos para mejorar")
    elif cal == 2:
        print("Gracias, seguiremos mejorando")
    elif cal == 3:
        print("Bien, pero aún podemos mejorar")
    elif cal == 4:
        print("Muy bien, gracias por su preferencia")
    elif cal == 5:
        print("Excelente, gracias por su valoración")
    else:
        print("Calificación inválida. Debe ser entre 1 y 5")
except ValueError:
    print("Entrada inválida: ingrese un número entero")