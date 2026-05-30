try:
    bateria = float(input("Ingrese el nivel de batería (%): "))
    
    if bateria < 0 or bateria > 100:
        print("Ingrese un porcentaje entre 0 y 100")
    elif bateria <= 30:
        print(f"Batería: {bateria}% - BAJA ⚠️ Cargar ahora")
    elif bateria <= 70:
        print(f"Batería: {bateria}% - MEDIA ⚡ Carga disponible")
    else:
        print(f"Batería: {bateria}% - ALTA ✓ Completamente cargado")
except ValueError:
    print("Entrada inválida: ingrese un número decimal")