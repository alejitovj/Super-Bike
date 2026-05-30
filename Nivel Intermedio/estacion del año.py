try:
    dia = int(input("Ingrese el día (1-31): "))
    mes = int(input("Ingrese el mes (1-12): "))
    
    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
        print("Fecha no válida")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
        print(f"{dia}/{mes}: PRIMAVERA")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 23):
        print(f"{dia}/{mes}: VERANO")
    elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        print(f"{dia}/{mes}: OTOÑO")
    else:
        print(f"{dia}/{mes}: INVIERNO")
except ValueError:
    print("Entrada inválida: ingrese números enteros")