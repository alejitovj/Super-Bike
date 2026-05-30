try:
    hijos = int(input("Ingrese la cantidad de hijos: "))
    salario = float(input("Ingrese el salario mensual: "))

    if hijos < 0 or salario < 0:
        print("Datos no válidos")
    elif hijos >= 3 and salario <= 2000000:
        print("Aplica subsidio alto")
    elif hijos >= 1 and salario <= 3000000:
        print("Aplica subsidio moderado")
    else:
        print("No aplica subsidio")
except ValueError:
    print("Ingrese valores numéricos válidos")