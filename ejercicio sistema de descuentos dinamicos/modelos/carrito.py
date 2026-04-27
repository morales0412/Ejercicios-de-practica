from .producto import Producto


class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise ValueError("El producto debe ser una instancia de la clase Producto")
        self._productos.append(producto)

    def filtrar_por_categoria(self, categoria):
        for producto in self._productos:
            if producto._categoria.lower() == categoria.lower():
                yield producto

    def simular_descuento(self, porcentaje):
        if not (0 <= porcentaje <= 1):
            raise ValueError(
                "El porcentaje de descuento debe estar entre 0 y 1 (0.15 = 15%)"
            )
        for producto in self._productos:
            precio_con_descuento = producto.precio_base * (1 - porcentaje)
            yield (producto.nombre, precio_con_descuento)

    def __len__(self):
        return len(self._productos)
