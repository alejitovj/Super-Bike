# Ingresar dos numeros y muestre cual es el mayor #
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

if num1 > num2:
        print(f"El numero {num1} es mayor")
elif num2 > num1:
        print(f"El numero {num2} es mayor")
else:
        print("Los numeros son iguales")

