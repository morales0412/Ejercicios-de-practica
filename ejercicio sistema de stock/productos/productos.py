from excepciones.excepcion_inventario import (
    StockInsuficienteError,
    CategoriaInvalidaError,
)


class Producto:
    categorias_validas = ["Smartphone", "Laptop", "Accesorio"]

    def __init__(self, id_producto, nombre, categoria, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria_ingresada):
        if categoria_ingresada.capitalize() not in self.categorias_validas:
            raise CategoriaInvalidaError(categoria_ingresada)
        self._categoria = categoria_ingresada

    def actualizar_stock(self, cantidad):
        if self.stock + cantidad < 0:
            raise StockInsuficienteError(self.nombre, cantidad, self.stock)
        self.stock += cantidad
