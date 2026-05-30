try:
    hora = int(input("Ingrese la hora (0-23): "))
    
    if hora < 0 or hora > 23:
        print("Ingrese una hora entre 0 y 23")
    elif hora >= 6 and hora < 12:
        print(f"Hora {hora}:00 - MAÑANA ☀️")
    elif hora >= 12 and hora < 18:
        print(f"Hora {hora}:00 - TARDE 🌤️")
    else:
        print(f"Hora {hora}:00 - NOCHE 🌙")
except ValueError:
    print("Entrada inválida: ingrese un número entero (0-23)")