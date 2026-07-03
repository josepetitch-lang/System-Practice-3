import time

def analizar_calidad_mensaje(mensaje: str):

    ruido_comun = ["eh", "bueno", "o sea", "básicamente", "no sé"]
    
    palabras = mensaje.lower().split()
    total_palabras = len(palabras)
    
    deteccion_ruido = [p for p in palabras if p in ruido_comun]
    porcentaje_ruido = (len(deteccion_ruido) / total_palabras) * 100 if total_palabras > 0 else 0
    
   
    print(f"Mensaje procesado: '{mensaje}'")
    print(f"Total tokens detectados: {total_palabras}")
    print(f"Nivel de ruido detectado: {porcentaje_ruido:.2f}%")
    
    if porcentaje_ruido < 10:
        print("Estado: Óptimo. La comunicación es clara y directa.")
    else:
        print("Estado: Alerta. Se recomienda reducir el uso de muletillas.")
    

if __name__ == "__main__":
    print("Iniciando analizador de flujo comunicativo (TBAT v1.0)...")
    user_input = input("Ingresa una frase para analizar: ")
    analizar_calidad_mensaje(user_input)