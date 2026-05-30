riesgo = input("Ingrese el nivel de riesgo (bajo/medio/alto): ").strip().lower()

if riesgo == "bajo":
    print("Recomendación: Mantener la prevención básica")
elif riesgo == "medio":
    print("Recomendación: Evitar zonas desoladas y estar alerta")
elif riesgo == "alto":
    print("Recomendación: No salir, buscar refugio seguro")
else:
    print("Nivel de riesgo no reconocido")