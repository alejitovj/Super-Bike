try:
    a = float(input("Digite el primer segmento: "))
    b = float(input("Digite el segundo segmento: "))
    c = float(input("Digite el tercer segmento: "))
    
    if a + b > c and a + c > b and b + c > a:
        print("Sí pueden formar un triángulo")
    else:
        print("No pueden formar un triángulo")
except ValueError:
    print("Entrada inválida: ingrese un número decimal")