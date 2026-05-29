try:
    año_nacimiento = int(input("Ingrese su año de nacimiento: "))
    
    año_actual = 2026
    
    if año_nacimiento < 1965:
        print(f"Año {año_nacimiento}: Generación anterior a X")
    elif año_nacimiento <= 1980:
        print(f"Año {año_nacimiento}: Generación X")
    elif año_nacimiento <= 1996:
        print(f"Año {año_nacimiento}: Millennial")
    elif año_nacimiento <= 2012:
        print(f"Año {año_nacimiento}: Generación Z")
    else:
        print(f"Año {año_nacimiento}: Generación posterior a Z (muy joven)")
except ValueError:
    print("Entrada inválida: ingrese un año válido")