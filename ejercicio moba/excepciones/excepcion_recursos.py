from .base import AccionInvalidaError


class FalloRecursosError(AccionInvalidaError):
    pass


class ManaInsuficienteError(FalloRecursosError):
    def __init__(self, mana_actual, mana_requerido):
        self.mana_actual = mana_actual
        self.mana_requerido = mana_requerido
        self.mana_faltante = mana_requerido - mana_actual
        mensaje = f"Mana insuficiente: Mana actual {self.mana_actual}, Mana requerido {self.mana_requerido}, Mana faltante {self.mana_faltante}"
        super().__init__(mensaje)


class OroInsuficienteError(FalloRecursosError):
    def __init__(self, oro_actual, oro_requerido):
        self.oro_actual = oro_actual
        self.oro_requerido = oro_requerido
        self.oro_faltante = oro_requerido - oro_actual
        mensaje = f"Oro insuficiente: Oro actual {self.oro_actual}, Oro requerido {self.oro_requerido}, Oro faltante {self.oro_faltante}"
        super().__init__(mensaje)
