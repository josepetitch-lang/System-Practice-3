class PymeState:
    def __init__(self, presupuesto_inicial=500, seguridad_inicial=30, cultura_inicial=20, reputacion_inicial=50):
        reflejan un negocio vulnerable en fase de diagnostico.
     
        self.presupuesto = presupuesto_inicial
        self.seguridad_red = seguridad_inicial
        self.cultura_pyme = cultura_inicial
        self.reputacion = reputacion_inicial
        self.turno_actual = 1
        self.game_over = False
        self.mensaje_final = ""

    def aplicar_impacto(self, impactos):
        
        self.presupuesto += impactos.get("presupuesto", 0)
        
        self.seguridad_red = max(0, min(100, self.seguridad_red + impactos.get("seguridad_red", 0)))
        self.cultura_pyme = max(0, min(100, self.cultura_pyme + impactos.get("cultura_pyme", 0)))
        self.reputacion = max(0, min(100, self.reputacion + impactos.get("reputacion", 0)))
        
        self.verificar_condiciones_criticas()

    def verificar_condiciones_criticas(self):
       
        if self.presupuesto <= 0:
            self.game_over = True
            self.mensaje_final = "QUIEBRA FINANCIERA: Te quedaste sin presupuesto para operar el negocio. El Plan DO falló por falta de liquidez."
        elif self.reputacion <= 10:
            self.game_over = True
            self.mensaje_final = "QUIEBRA DE REPUTACIÓN: La comunidad perdió total confianza en el abasto debido a los incidentes de seguridad. Nadie vuelve a comprar aquí."

    def procesar_ataque_aleatorio(self, ataque):
       
        requisito = ataque["requisito"]
        valor_actual = getattr(self, requisito)
        
        if valor_actual >= ataque["umbral"]:
            return True, ataque["exito"]
        else:
            self.aplicar_impacto(ataque["daño"])
            return False, ataque["fallo"]

    def avanzar_turno(self):
        """ Incrementa el contador de ciclos del juego. """
        self.turno_actual += 1

# we're screwed
