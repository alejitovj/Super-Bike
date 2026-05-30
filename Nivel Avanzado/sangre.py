tipo = input("Ingrese su tipo de sangre (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip().upper()

donantes = {
    "A+": ["A+", "A-", "O+", "O-"],
    "A-": ["A-", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "B-": ["B-", "O-"],
    "AB+": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
    "AB-": ["A-", "B-", "AB-", "O-"],
    "O+": ["O+", "O-"],
    "O-": ["O-"]
}

if tipo in donantes:
    print(f"Puede recibir de: {', '.join(donantes[tipo])}")
else:
    print("Tipo de sangre no reconocido")