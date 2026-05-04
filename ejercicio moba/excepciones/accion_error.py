from .base import MobaError


class AccionError(MobaError):
    pass


class HabilidadEnfriamientoError(AccionError):
    def __init__(self, tiempo_restante):
        self.tiempo_restante = tiempo_restante
        mensaje = f"Habilidad disponible en {self.tiempo_restante:.2f} segundos"
        super().__init__(mensaje)


class ManaInsuficienteError(AccionError):
    def __init__(self, costo_mana, mana_actual):
        self.costo_mana = costo_mana
        self.mana_actual = mana_actual
        mensaje = f"Mana insuficiente, costo mana: {self.costo_mana} | actual: {self.mana_actual}"
        super().__init__(mensaje)


class EstadoIncapacitadoError(AccionError):
    def __init__(self, estado):
        self.estado = estado
        mensaje = f"Accion no permitida mientras estas {self.estado}"
        super().__init__(mensaje)
