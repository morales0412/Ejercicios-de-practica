class ProductoNoEncontradoError(Exception):
    def __init__(self, nombre_producto):
        self.nombre_producto = nombre_producto
        mensaje = (
            f"El producto '{self.nombre_producto}' no se encuentra en el inventario."
        )
        super().__init__(mensaje)


class StockInsuficienteError(Exception):
    def __init__(self, stock_actual, cantidad_requerida):
        self.stock_actual = stock_actual
        self.cantidad_requerida = cantidad_requerida
        self.faltante = self.cantidad_requerida - self.stock_actual
        mensaje = f"Stock insuficiente, Faltan {self.faltante} unidades"
        super().__init__(mensaje)


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"] == nombre:
                producto["cantidad"] += cantidad
                return
        self.productos.append({"nombre": nombre, "cantidad": cantidad})

    def buscar_producto(self, nombre):
        if not self.productos:
            raise ValueError("El inventario esta vacio")
        for producto in self.productos:
            if producto["nombre"] == nombre:
                return producto
        raise ProductoNoEncontradoError(nombre)

    def vender_producto(self, nombre, cantidad):

        producto = self.buscar_producto(nombre)
        if cantidad > producto["cantidad"]:
            raise StockInsuficienteError(producto["cantidad"], cantidad)
        producto["cantidad"] -= cantidad


inventario = Inventario()
inventario.agregar_producto("camisa", 10)
inventario.agregar_producto("pantalon", 5)

try:
    inventario.vender_producto("camisa", 3)
except StockInsuficienteError as e:
    print(e)
finally:
    print(inventario.productos)

try:
    inventario.vender_producto("zapatos", 1)
except ProductoNoEncontradoError as e:
    print(e)
# ProductoNoEncontradoError: El producto "zapatos" no existe en el inventario
