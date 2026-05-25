num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el primer numero: "))

print("Seleccione una operacion: ")
print("1. Sumar: ")
print("2. Restar: ")
print("3. Multiplicar: ")
print("4. Dividir: ")

opcion = input("Digite una opcion 1(/2/3/4): ")

if opcion == "1":
    resultado = num1 + num2
    print("La suma es: ", resultado)

elif opcion == "2":
    resultado = num1 - num2
    print("La resta es: ", resultado)

elif opcion == "3":
    resultado = num1 * num2
    print("La multiplicacion es: ", resultado)

elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("La division es: ", resultado)
    else:
        print("No se puede dividir entre cero ")
        
else:
    print("Opcion no válida")
