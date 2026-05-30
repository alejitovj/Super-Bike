try:
    n = int(input("Ingrese un número: "))
    
    digitos = len(str(abs(n)))  # abs() para trabajar con valor positivo
    
    if digitos == 1:
        print(f"{n} tiene 1 dígito")
    elif digitos == 2:
        print(f"{n} tiene 2 dígitos")
    elif digitos == 3:
        print(f"{n} tiene 3 dígitos")
    else:
        print(f"{n} tiene {digitos} dígitos")
except ValueError:
    print("Entrada inválida: ingrese un número entero")