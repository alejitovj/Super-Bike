def pedir_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

a = pedir_numero("Digite el primer número: ")
b = pedir_numero("Digite el segundo número: ")
c = pedir_numero("Digite el tercer número: ")

menor = min(a, b, c)
print(f"El número menor es: {menor}")