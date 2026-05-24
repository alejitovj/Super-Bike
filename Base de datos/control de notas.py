nombre = input("Digite su nombre: ")

# Nota definitiva de estudiante #
nota1 = float(input("Digite su primera nota: "))
nota2 = float(input("Digite su segunda nota: "))
nota3 = float(input("Digite su tercera nota: "))
nota4 = float(input("Digite su cuarta nota: "))
nota5 = float(input("Digite su ultima nota: "))

definitiva = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if definitiva >=3:
    print("Usted ha sido aprobado señor: ", nombre)
else:
    print(f"Señor {nombre} lastimosamente usted ha sido reprobado")