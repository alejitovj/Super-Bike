try:
    hora = int(input("Ingrese una hora en formato 24h (0-23): "))
    if hora < 0 or hora > 23:
        print("Hora no válida")
    elif hora < 12:
        print("Buenos días")
    elif hora < 18:
        print("Buenas tardes")
    else:
        print("Buenas noches")
except ValueError:
    print("Ingrese una hora válida")