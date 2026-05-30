letra = input("Ingrese una letra: ").lower()

vocales = "aeiouáéíóú"

if len(letra) != 1:
    print("Ingrese solo una letra")
elif not letra.isalpha():
    print("Ingrese una letra válida")
elif letra in vocales:
    print(f"'{letra}' es una VOCAL")
else:
    print(f"'{letra}' es una CONSONANTE")