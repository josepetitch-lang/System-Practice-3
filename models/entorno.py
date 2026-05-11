class Entorno:
    def __init__(self, evento, factor_demanda, costo_material):
        self.evento = evento
        self.factor_demanda = factor_demanda
        self.costo_material = costo_material

    def __str__(self):
        return f"Entorno :{self.evento} | Demanda: {self.factor_demanda} | Costo: {self.costo_material}"