class Item:
    def __init__(self, nombre, tipo, precio, bonificaciones):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.bonificaciones = bonificaciones

    def mostrar_bonificaciones(self):
        return ", ".join(
            f"{stat}: +{valor}" for stat, valor in self.bonificaciones.items()
        )

    def __str__(self):
        return f"{self.nombre} - Tipo: {self.tipo}, Precio: {self.precio}, Bonificaciones: {self.mostrar_bonificaciones()}"
