from .plan_base import PlanBase


class PlanAnual(PlanBase):
    def __init__(self, precio_base, descuento):
        self.precio_base = precio_base
        self.descuento = descuento

    def obtener_costo(self):
        return (self.precio_base * 12) * (1 - self.descuento)

    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, valor):
        if not (0 <= valor <= 1):
            raise ValueError("El descuento debe estar entre 0 y 1")
        self._descuento = valor
