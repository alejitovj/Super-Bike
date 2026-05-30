try:
    cantidad = int(input("Ingrese la cantidad de productos comprados: "))
    if cantidad < 0:
        print("Cantidad no válida")
    elif cantidad >= 10:
        print("Aplica promoción de descuento")
    else:
        print("No aplica promoción")
except ValueError:
    print("Entrada inválida: ingrese un número entero")