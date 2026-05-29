try:
    horas = float(input("Ingrese las horas trabajadas: "))
    
    horas_normales = 40
    valor_hora_normal = 15000  # ajustable
    valor_hora_extra = valor_hora_normal * 1.5  # 50% más
    
    if horas < 0:
        print("Las horas no pueden ser negativas")
    elif horas <= horas_normales:
        pago = horas * valor_hora_normal
        print(f"Horas trabajadas: {horas}")
        print(f"No hay horas extras")
        print(f"Total a pagar: ${pago:,.0f}")
    else:
        horas_extra = horas - horas_normales
        pago_normal = horas_normales * valor_hora_normal
        pago_extra = horas_extra * valor_hora_extra
        pago_total = pago_normal + pago_extra
        
        print(f"Horas normales (40): ${pago_normal:,.0f}")
        print(f"Horas extras ({horas_extra}): ${pago_extra:,.0f}")
        print(f"Total a pagar: ${pago_total:,.0f}")
except ValueError:
    print("Entrada inválida: ingrese un número decimal")