from excepciones.excepciones_descuentos import NegativePriceError


class Producto:
    def __init__(self, nombre, precio_base, categoria, ean13, **kwargs):
        self._nombre = nombre
        self.precio_base = precio_base
        self._categoria = categoria
        if not self.verificar_ean13(ean13):
            raise ValueError(f"El codigo {ean13} no es valido")
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
        return len(ean13) == 13 and ean13.isdigit()

    def __str__(self):
        return f"{self.nombre}-{self.categoria}-${self.precio_base}-EAN13:{self.ean13}"

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def ean13(self):
        return self._ean13
