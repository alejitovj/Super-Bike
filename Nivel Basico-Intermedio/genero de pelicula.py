genero = input("Ingrese el género de película (acción, drama, comedia, terror): ").lower()

if genero == "acción":
    print("Recomendación: Avengers - Endgame")
elif genero == "drama":
    print("Recomendación: El Padrino")
elif genero == "comedia":
    print("Recomendación: Superbad")
elif genero == "terror":
    print("Recomendación: El Exorcista")
else:
    print("Género no reconocido")