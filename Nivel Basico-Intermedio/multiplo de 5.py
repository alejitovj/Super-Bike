try:
    n = int(input("Ingrese un número: "))
    
    if n % 5 == 0:
        print(f"{n} es múltiplo de 5")
    else:
        print(f"{n} NO es múltiplo de 5")
except ValueError:
    print("Entrada inválida: ingrese un número entero")