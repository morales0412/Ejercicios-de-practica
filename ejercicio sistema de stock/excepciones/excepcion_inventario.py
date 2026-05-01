from .base import InventarioException


class StockInsuficienteError(InventarioException):
    def __init__(self, producto, solicitado, disponible):
        self.producto = producto
        self.solicitado = solicitado
        self.disponible = disponible
        mensaje = f"Stock insuficiente para {producto}. Solicitado: {solicitado}, Disponible: {disponible}"
        super().__init__(mensaje)


class ProductoNoEncontradoError(InventarioException):
    def __init__(self, id_producto):
        self.id_producto = id_producto
        mensaje = f"Producto con ID {id_producto} no encontrado en el inventario"
        super().__init__(mensaje)


class CategoriaInvalidaError(InventarioException):
    def __init__(self, categoria):
        self.categoria = categoria
        mensaje = f"Categoria '{categoria} no es valida"
        super().__init__(mensaje)
