operador = input("Ingrese su operador móvil: ").strip().lower()

if operador == "claro":
    print("Beneficio: 10% de descuento en recargas")
elif operador == "movistar":
    print("Beneficio: 5GB extra en tu próxima recarga")
elif operador == "tigo":
    print("Beneficio: llamadas ilimitadas por un día")
else:
    print("Operador no reconocido")