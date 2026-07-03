class SimuladorComunicacion:
    def __init__(self):
        self.ruido = 0.2  

    def procesar_mensaje(self, mensaje, nivel_ruido):
        
        if nivel_ruido > 0.7:
            return "[ERROR]: Mensaje perdido por ruido excesivo."
        elif nivel_ruido > 0.4:
            return f"[ADVERTENCIA]: Mensaje distorsionado: {mensaje[::-1]}" # voltea el texto
        else:
            return f"[OK]: Mensaje recibido: {mensaje}"