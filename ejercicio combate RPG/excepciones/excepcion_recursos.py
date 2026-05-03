from .base import AccionInvalidaError


class FalloRecursoError(AccionInvalidaError):
    pass


class ManaInsuficienteError(FalloRecursoError):
    def __init__(self, mana_actual, mana_requerido):
        self.mana_actual = mana_actual
        self.mana_requerido = mana_requerido
        mensaje = f"Mana insuficiente: {self.mana_actual} disponible, requerido {self.mana_requerido}"
        super().__init__(mensaje)


class FatigaExtremaError(FalloRecursoError):
    def __init__(self, fatiga_actual, fatiga_maxima):
        self.fatiga_actual = fatiga_actual
        self.fatiga_maxima = fatiga_maxima
        mensaje = f"Estás al borde del colapso físico , fatiga actual: {self.fatiga_actual}/{self.fatiga_maxima}"
        super().__init__(mensaje)
