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

    def __str__(self):
        stats_str = ", ".join(f"{key}: {value}" for key, value in self.stats.items())
        return f"{self.nombre} - Precio: {self.precio} - Stats: {stats_str}"


class Posion(Item):
    def __init__(self, nombre, precio, curacion):
        super().__init__(nombre, precio)
        self.stats["curacion"] = curacion

    def __str__(self):
        return super().__str__()
