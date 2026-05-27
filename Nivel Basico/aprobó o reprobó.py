nota1 = int(input("Digite la primera nota: "))
nota2 = int(input("Digite la segunda nota: "))
nota3 = int(input("Digite la tercera nota: "))
nota4 = int(input("Digite la cuarta nota: "))
nota5 = int(input("Digite la quinta nota: "))


definitiva = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if definitiva >= 3.0:
    print(f"Abropó. Nota definitiva: {definitiva:.1f}")
else:
    print(f"Reprobó. Nota definitiva {definitiva:.1f}")
