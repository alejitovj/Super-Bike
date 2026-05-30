try:
    x = float(input("Digite el primer número: "))
    y = float(input("Digite el segundo número: "))
    z = float(input("Digite el tercer número: "))
    
    if x <= y <= z:
        print("Están en orden ascendente")
    else:
        print("No están en orden ascendente")
except ValueError:
    print("Entrada inválida: ingrese un número decimal")