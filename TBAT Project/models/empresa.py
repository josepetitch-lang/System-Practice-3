class Empresa:
    def __init__(self, capital_restante):
        self.capital_restante = capital_restante

class Empresa_Estatica(Empresa):
    def __init__(self, capital, produccion_fila, costo_operativo):
        super().__init__(capital)
        self.produccion_fila = produccion_fila
        self.costo_operativo = costo_operativo

    def procesar_ciclo(self, entorno):
        gasto = self.costo_operativo + entorno.costo_material
        self.capital_restante -= gasto
        return self.capital_restante

class Empresa_Adaptativa(Empresa):
    def __init__(self, capital, produccion_ajustada, costo_optimizado):
        super().__init__(capital)
        self.produccion_ajustada = produccion_ajustada
        self.costo_optimizado = costo_optimizado

    def procesar_ciclo(self, entorno, nivel_capacitacion=0.1):
        self.produccion_ajustada = 100 * entorno.factor_demanda
        eficiencia = 1.0 + (nivel_capacitacion / 100)
        self.costo_optimizado = (entorno.costo_material + 15) / eficiencia

        self.capital_restante -= self.costo_optimizado
        
        
        return self.capital_restante, self.produccion_ajustada