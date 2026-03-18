class GestorPedidos:
    
    def __init__(self):
        self.__inventario_por_producto = {}
        self.__pedidos_activos = []
    
    def registrar_producto(self, producto):
        if producto.id in self.__inventario_por_producto:
            self.__inventario_por_producto[producto.id].append(producto)
        else:
            self.__inventario_por_producto[producto.id] = [producto]