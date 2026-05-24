# Validar ingreso correcto #
nombre = input("Digite su nombre: ")
clave_correcta = "abc123"
intentos = 0
acceso = False

while intentos < 3 and not acceso:
    clave_usuario = input("Ingrese la contraseña: ")
    if clave_usuario == clave_correcta:
        acceso = True
    else:
        intentos += 1
        print("Contraseña incorrecta. Intentos restantes: ", 3 - intentos)

if acceso:
    print("Bienvenido ", nombre)
    print("Ingreso exitoso")
else:
    print("Acceso denegado")