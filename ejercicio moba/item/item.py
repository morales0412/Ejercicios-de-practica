class Item:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.stats = {}

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor
