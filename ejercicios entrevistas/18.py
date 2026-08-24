from functools import reduce


class PedidoError(Exception):
    def __init__(self, nombre_producto, cantidad_solicitada, cantidad_disponible):
        self.nombre_producto = nombre_producto
        self.cantidad_solicitada = cantidad_solicitada
        self.cantidad_disponible = cantidad_disponible
        self.cantitdad_faltante = cantidad_solicitada - cantidad_disponible
        mensaje = f"El producto '{nombre_producto}' no tiene suficiente stock. Cantidad solicitada: {cantidad_solicitada}, Cantidad disponible: {cantidad_disponible}. Faltan {self.cantitdad_faltante} unidades."
        super().__init__(mensaje)


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacio.")

        if len(valor) > 50:
            raise ValueError(
                "El nombre del producto no puede tener mas de 50 caracteres."
            )
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("El precio debe ser un numero")

        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        self._precio = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if not isinstance(valor, int):
            raise ValueError("El stock debe ser un numero entero")

        if valor < 0:
            raise ValueError("El stock no puede ser negativo")

        self._stock = valor

    def reducir_stock(self, cantidad):

        if not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un numero entero")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")

        if cantidad > self.stock:
            raise PedidoError(self.nombre, cantidad, self.stock)
        self.stock -= cantidad

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.estado = "pendiente"

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El nombre del cliente debe ser una cadena de texto")

        if valor.strip() == "":
            raise ValueError("El nombre del cliente no puede estar vacio")

        self._cliente = valor

    def agregar_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise ValueError("El producto debe ser una instancia de la clase Producto")

        if not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un numero entero")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")

        self.productos.append((producto, cantidad))

    def calcular_total(self):

        if not self.productos:
            raise ValueError("No hay productos en el pedido")

        total = reduce(
            lambda acc, item: acc + item[0].precio * item[1], self.productos, 0
        )
        return total

    def confirmar(self):
        for producto, cantidad in self.productos:
            if cantidad > producto.stock:
                raise PedidoError(producto.nombre, cantidad, producto.stock)
        for producto, cantidad in self.productos:
            producto.reducir_stock(cantidad)
        self.estado = "confirmado"

    def resumen(self):
        productos = [
            {"nombre": producto.nombre, "cantidad": cantidad}
            for producto, cantidad in self.productos
        ]
        return {
            "cliente": self.cliente,
            "total": self.calcular_total(),
            "estado": self.estado,
            "productos": productos,
        }

    def __str__(self):
        return f"Cliente: {self.cliente} | Estado: {self.estado} | Total: {self.calcular_total()}"


p1 = Producto("Camisa", 50000, 10)
p2 = Producto("Pantalon", 80000, 3)

pedido = Pedido("Ana")
pedido.agregar_producto(p1, 2)
pedido.agregar_producto(p2, 5)

try:
    pedido.confirmar()
except PedidoError as e:
    print(e)
# PedidoError: No hay suficiente stock de Pantalon. Código: STOCK_INSUFICIENTE

pedido2 = Pedido("Luis")
pedido2.agregar_producto(p1, 2)
pedido2.confirmar()
print(pedido2.resumen())
# {
#     "cliente": "Luis",
#     "total": 100000,
#     "estado": "confirmado",
#     "productos": [{"nombre": "Camisa", "cantidad": 2}]
# }
