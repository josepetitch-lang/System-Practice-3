def calcular_desviacion(cap_estatica, cap_adaptativa):
    desviacion = cap_adaptativa - cap_estatica
    mensaje = "Estabilidad detectada"

    if desviacion > 0:
        mensaje = f"El sistema adaptativo preservó ${desviacion:.2f} más que el estático"
    else:
        mensaje = "Ambos sistemas pierden"

    return desviacion, mensaje