from excepciones.excepcion_inventario import ProductoNoEncontradoError


class Bodega:
    def __init__(self):
        self.inventario = {}
        self.categorias = set()

    def agregar_producto(self, producto):
        if producto.id_producto in self.inventario:
            raise ValueError(
                f"El producto con ID {producto.id_producto} ya existe en el inventario"
            )
        self.inventario[producto.id_producto] = producto
        self.categorias.add(producto.categoria)

    def vender_producto(self, id_producto, cantidad):
        if id_producto not in self.inventario:
            raise ProductoNoEncontradoError(id_producto)
        producto = self.inventario[id_producto]
        producto.actualizar_stock(-cantidad)

    def mostrar_informe(self):
        if not self.inventario:
            print("El inventario esta vacio")

        for producto in self.inventario.values():
            print(
                f"ID: {producto.id_producto}, Nombre: {producto.nombre}, categoria: {producto.categoria}, Precio: {producto.precio}, Stock: {producto.stock}"
            )
