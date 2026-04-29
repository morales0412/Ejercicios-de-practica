from .plan_base import PlanBase


class PlanMensual(PlanBase):
    def __init__(self, precio_base):
        self.precio_base = precio_base

    def obtener_costo(self):
        return self.precio_base
