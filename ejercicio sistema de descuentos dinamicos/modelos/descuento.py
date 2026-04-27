from abc import ABC, abstractmethod
from excepciones.excepciones_descuentos import NegativePriceError


class Descuento(ABC):
    @abstractmethod
    def aplicar_descuento(self, precio):
        pass


class FlatDescuento(Descuento):
    def __init__(self, monto_descuento):
        if monto_descuento < 0:
            raise NegativePriceError(monto_descuento)
        self.monto_descuento = monto_descuento

    def aplicar_descuento(self, precio):
        precio_con_descuento = precio - self.monto_descuento
        if precio_con_descuento < 0:
            raise NegativePriceError(precio_con_descuento)
        return precio_con_descuento


class PercentageDescuento(Descuento):
    def __init__(self, porcentaje_descuento):
        if not (0 <= porcentaje_descuento <= 1):
            raise ValueError(
                "El porcentaje de descuent debe estar entre 0 y 1 (0.15 = 15%)"
            )
        self.porcentaje_descuento = porcentaje_descuento

    def aplicar_descuento(self, precio):
        precio_con_descuento = precio * (1 - self.porcentaje_descuento)
        if precio_con_descuento < 0:
            raise NegativePriceError(precio_con_descuento)
        return precio_con_descuento
