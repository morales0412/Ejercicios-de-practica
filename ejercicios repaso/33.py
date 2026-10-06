from functools import reduce


class ProductoNoEncontradoError(Exception):
    def __init__(self, nombre_producto):
        self.nombre_producto = nombre_producto
        mensaje = f"El producto '{nombre_producto}' no se encuentra en el carrito."
        super().__init__(mensaje)


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad=1) -> None:
        """Agrega un producto al carrito de compras. Si el producto ya existe, se actualiza la cantidad."""
        if any(producto["nombre"] == nombre for producto in self.productos):
            for producto in self.productos:
                if producto["nombre"] == nombre:
                    producto["cantidad"] += cantidad
                    print(
                        f" Se ha actualizado la cantidad del producto '{nombre} a {producto['cantidad']} unidades."
                    )
        else:
            producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
            self.productos.append(producto)
            print(f" Se ha agregado el producto '{nombre}' al carrito.")

    def eliminar_producto(self, nombre) -> None:
        """Elimina un producto del carrito de compras por su nombre. Si el producto no se encuentra en el carrito, lanza una excepcion"""
        if not self.productos:
            print(" El carrito esta vacio. No hay productos para eliminar.")
            return
        if any(producto["nombre"] == nombre for producto in self.productos):
            for producto in self.productos:
                if producto["nombre"] == nombre:
                    self.productos.remove(producto)
                    print(f" Se ha eliminado el producto '{nombre}' del carrito.")
        else:
            raise ProductoNoEncontradoError(nombre)

    def calcular_total(self) -> float:
        """Calcula el total del carrito de compras multiplicando el precio por la cantidad de cada producto y sumando los resultados."""
        if not self.productos:
            print("El carrito esta vacio. No hay productos para calcular el total.")
            return 0
        total = reduce(
            lambda acc, producto: acc + (producto["precio"] * producto["cantidad"]),
            self.productos,
            0,
        )
        return total

    def aplicar_cupones(self, *cupones) -> float:
        """Aplica los cupones de descuento al total del carrido. Cada cupon es acomulable y se devuelve el total final con los descuentos aplicados."""
        if not self.productos:
            print("No hay productos para aplicarle cupones")
            return 0
        total = self.calcular_total()
        for cupon in cupones:
            total = total * (1 - cupon / 100)
        return total

    def resumen(self, **kwargs) -> dict:
        """
        Devuelve un diccionario con el total del carrito y cualquier otro argumento adicional pasado como keyword arguments."""
        return {"total": self.calcular_total(), **kwargs}
