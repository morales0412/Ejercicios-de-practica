from excepciones.excepciones_descuentos import NegativePriceError


class Producto:
    def __init__(self, nombre, precio_base, categoria, ean13, **kwargs):
        self._nombre = nombre
        self._precio_base = precio_base
        self._categoria = categoria
        self._ean13 = ean13
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, nuevo_precio):
        if nuevo_precio < 0:
            raise NegativePriceError(nuevo_precio)
        self._precio_base = nuevo_precio

    @staticmethod
    def verificar_ean13(ean13):
        if len(ean13) != 13 or not ean13.isdigit():
            raise ValueError("El codigo EAN13 debe tener 13 digitos numericos")
