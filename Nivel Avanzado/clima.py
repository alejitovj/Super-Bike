try:
    estado = input("Ingrese el estado del clima (soleado, lluvioso, nublado): ").strip().lower()
    temp = float(input("Ingrese la temperatura actual en °C: "))

    if estado == "soleado":
        ropa = "ropa ligera"
    elif estado == "lluvioso":
        ropa = "ropa impermeable"
    else:
        ropa = "ropa cómoda"

    if temp <= 15:
        ropa = "ropa abrigada"
    elif temp >= 30:
        ropa = "ropa fresca"

    if estado == "lluvioso":
        paraguas = "Sí, lleva sombrilla"
    else:
        paraguas = "No, no necesitas sombrilla"

    if estado == "lluvioso" or temp < 10:
        aire_libre = "No es recomendable"
    else:
        aire_libre = "Sí, puedes hacer actividades al aire libre"

    print(f"Recomendación: {ropa}")
    print(paraguas)
    print(aire_libre)
except ValueError:
    print("Ingrese una temperatura válida")