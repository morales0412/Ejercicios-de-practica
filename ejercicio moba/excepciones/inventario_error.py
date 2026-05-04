from .base import MobaError


class InventarioError(MobaError):
    pass


class OroInsuficienteError(InventarioError):
    def __init__(self, oro_faltante):
        self.oro_faltante = oro_faltante
        mensaje = f"Oro insuficiente, te faltan {self.oro_faltante}"
        super().__init__(mensaje)


class InventarioLlenoError(InventarioError):
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        mensaje = f"Inventario lleno, capacidad maxima de {self.capacidad_maxima} items"
        super().__init__(mensaje)
