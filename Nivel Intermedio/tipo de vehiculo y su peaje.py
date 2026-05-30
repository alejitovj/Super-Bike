tipo_vehiculo = input("Ingrese el tipo de vehículo (auto, moto, bus, camión): ").lower()

peajes = {
    "auto": 3500,
    "moto": 1500,
    "bus": 8000,
    "camión": 10000
}

if tipo_vehiculo in peajes:
    print(f"Vehículo: {tipo_vehiculo.capitalize()}")
    print(f"Peaje a pagar: ${peajes[tipo_vehiculo]:,.0f}")
else:
    print("Tipo de vehículo no reconocido")