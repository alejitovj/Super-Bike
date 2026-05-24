nombre = input("Digite su nombre por favor: ")
edad = int(input("Digite su edad: "))

if edad < 0:
    print("Edad no válida")
elif edad <= 12:
    print("Clasificacion: Niño")
elif edad <= 17:
    print("Clasificacion: Adolescente")
elif edad <= 39:
    print("Clasificacion: Adulto")
elif edad <= 59:
    print("Clasificacion: Adulto mayor")
else:
    print("Abuelo")