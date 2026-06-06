# SISTEMA INTEGRADO DE 5 ACTIVIDADES

def autenticacion():
    """Actividad 1: Sistema de autenticación de usuarios"""
    contraseña_correcta = "SENA123"
    print("\n--- ACTIVIDAD 1: AUTENTICACIÓN ---")
    
    while True:
        contraseña = input("Ingrese la contraseña: ")
        if contraseña == contraseña_correcta:
            print("¡Acceso permitido! Bienvenido al sistema.")
            break
        else:
            print("Contraseña incorrecta. Intente de nuevo.")

def inventario():
    """Actividad 2: Registro de productos en inventario"""
    print("\n--- ACTIVIDAD 2: INVENTARIO ---")
    productos = []
    
    while True:
        nombre = input("Ingrese nombre del producto (o 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break
        
        try:
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            
            productos.append({
                "nombre": nombre,
                "cantidad": cantidad,
                "precio": precio
            })
            print("Producto registrado exitosamente.\n")
        except ValueError:
            print("Ingrese valores numéricos válidos.\n")
    
    print("\n--- RESUMEN DEL INVENTARIO ---")
    for i, prod in enumerate(productos, 1):
        print(f"{i}. {prod['nombre']} - Cantidad: {prod['cantidad']} - Precio: ${prod['precio']:,.2f}")
    print(f"Total de productos: {len(productos)}")

def factura():
    """Actividad 3: Generación de facturas de venta"""
    print("\n--- ACTIVIDAD 3: FACTURA DE VENTA ---")
    productos = []
    total = 0
    
    while True:
        try:
            nombre = input("Ingrese nombre del producto (o 'finalizar' para terminar): ")
            if nombre.lower() == "finalizar":
                break
            
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio unitario: "))
            
            subtotal = cantidad * precio
            total += subtotal
            
            productos.append({
                "nombre": nombre,
                "cantidad": cantidad,
                "precio": precio,
                "subtotal": subtotal
            })
            print("Producto agregado a la factura.\n")
        except ValueError:
            print("Ingrese valores válidos.\n")
    
    print("\n--- FACTURA DE VENTA ---")
    print("-" * 50)
    for prod in productos:
        print(f"{prod['nombre']}: {prod['cantidad']} x ${prod['precio']:,.2f} = ${prod['subtotal']:,.2f}")
    print("-" * 50)
    print(f"TOTAL A PAGAR: ${total:,.2f}")

def asistencia():
    """Actividad 4: Control de asistencia"""
    print("\n--- ACTIVIDAD 4: CONTROL DE ASISTENCIA ---")
    
    try:
        num_personas = int(input("Ingrese cantidad de personas: "))
        asistentes = 0
        ausentes = 0
        
        for i in range(1, num_personas + 1):
            nombre = input(f"Nombre de persona {i}: ")
            estado = input(f"¿{nombre} asistió? (sí/no): ").strip().lower()
            
            if estado == "sí" or estado == "si":
                asistentes += 1
            else:
                ausentes += 1
        
        print("\n--- REPORTE DE ASISTENCIA ---")
        print(f"Total de personas: {num_personas}")
        print(f"Asistentes: {asistentes}")
        print(f"Ausentes: {ausentes}")
        print(f"Porcentaje de asistencia: {(asistentes/num_personas)*100:.1f}%")
    except ValueError:
        print("Ingrese un número válido.")

def menu_gestion():
    """Actividad 5: Menú principal de un sistema de gestión"""
    print("\n--- ACTIVIDAD 5: MENÚ DE GESTIÓN ---")
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar usuario")
        print("2. Consultar información")
        print("3. Actualizar datos")
        print("4. Eliminar registro")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            nombre = input("Ingrese nombre del usuario: ")
            print(f"Usuario '{nombre}' registrado exitosamente.")
        elif opcion == "2":
            usuario = input("Ingrese nombre del usuario a consultar: ")
            print(f"Información del usuario '{usuario}' consultada.")
        elif opcion == "3":
            usuario = input("Ingrese nombre del usuario a actualizar: ")
            print(f"Datos de '{usuario}' actualizados exitosamente.")
        elif opcion == "4":
            usuario = input("Ingrese nombre del usuario a eliminar: ")
            print(f"Usuario '{usuario}' eliminado exitosamente.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_principal():
    """Menú para seleccionar qué actividad ejecutar"""
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE ACTIVIDADES - NIVEL AVANZADO")
        print("="*50)
        print("1. Autenticación de usuarios")
        print("2. Registro de inventario")
        print("3. Generación de facturas")
        print("4. Control de asistencia")
        print("5. Sistema de gestión (menú)")
        print("6. Salir del programa")
        print("="*50)
        
        opcion = input("Seleccione una actividad (1-6): ")
        
        if opcion == "1":
            autenticacion()
        elif opcion == "2":
            inventario()
        elif opcion == "3":
            factura()
        elif opcion == "4":
            asistencia()
        elif opcion == "5":
            menu_gestion()
        elif opcion == "6":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()