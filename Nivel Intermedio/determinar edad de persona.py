try:
    edad = int(input("Ingrese la edad: "))
    
    if edad < 0:
        print("Edad no válida")
    elif edad <= 2:
        print(f"Edad {edad}: Bebé")
    elif edad <= 12:
        print(f"Edad {edad}: Niño")
    elif edad <= 17:
        print(f"Edad {edad}: Adolescente")
    elif edad <= 30:
        print(f"Edad {edad}: Adulto joven")
    elif edad <= 60:
        print(f"Edad {edad}: Adulto")
    else:
        print(f"Edad {edad}: Adulto mayor")
except ValueError:
    print("Entrada inválida: ingrese un número entero")