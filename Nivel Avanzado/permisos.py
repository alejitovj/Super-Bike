rol = input("Ingrese el rol del usuario (admin, editor, invitado): ").strip().lower()

if rol == "admin":
    print("Permisos: leer, escribir, eliminar, configurar")
elif rol == "editor":
    print("Permisos: leer, escribir")
elif rol == "invitado":
    print("Permisos: leer")
else:
    print("Rol no reconocido")