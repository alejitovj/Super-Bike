try:
    estrato = int(input("Ingrese su estrato social (1-6): "))
    
    if estrato == 1:
        print("Estrato 1: Subsidio del 100%")
    elif estrato == 2:
        print("Estrato 2: Subsidio del 80%")
    elif estrato == 3:
        print("Estrato 3: Subsidio del 50%")
    elif estrato == 4:
        print("Estrato 4: Subsidio del 20%")
    elif estrato in [5, 6]:
        print(f"Estrato {estrato}: Subsidio del 0%")
    else:
        print("Estrato inválido. Ingrese un número entre 1 y 6")
except ValueError:
    print("Entrada inválida: ingrese un número entero")