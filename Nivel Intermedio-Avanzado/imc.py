try:
    imc = float(input("Ingrese su IMC: "))
    if imc <= 0:
        print("IMC no válido")
    elif imc < 25:
        print("Bajo peso")
    elif imc < 50:
        print("Peso normal")
    elif imc < 80:
        print("Sobrepeso")
    else:
        print("Obesidad")
except ValueError:
    print("Entrada inválida: ingrese un número")