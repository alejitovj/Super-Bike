color = input("Ingrese el color del semáforo (rojo, amarillo, verde): ").lower()

if color == "rojo":
    print("Acción: DETENTE - Espera el cambio de luz")
elif color == "amarillo":
    print("Acción: PRECAUCIÓN - Prepárate para detenerte")
elif color == "verde":
    print("Acción: ADELANTE - Puedes cruzar")
else:
    print("Color no válido. Ingrese rojo, amarillo o verde")