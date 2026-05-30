try:
    puntaje = int(input("Ingrese el puntaje del videojuego: "))
    
    if puntaje < 0:
        print("El puntaje no puede ser negativo")
    elif puntaje < 1000:
        print(f"Puntaje: {puntaje} - NOVATO 🟢 Sigue practicando")
    elif puntaje <= 5000:
        print(f"Puntaje: {puntaje} - INTERMEDIO 🟡 Buen nivel")
    else:
        print(f"Puntaje: {puntaje} - EXPERTO 🔴 ¡Maestro!")
except ValueError:
    print("Entrada inválida: ingrese un número entero")