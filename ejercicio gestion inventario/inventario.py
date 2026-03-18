class Inventario:
    
    def __init__(self):
        self.__productos = []
    
    def agregar_producto(self,producto):
        self.__productos.append(producto)
    
    def calcular_valor_total(self):
        if not self.__productos:
            return 0
        return sum(p.precio * p.cantidad for p in self.__productos)
        
    def mostrar_productos_criticos(self):
        for producto in self.__productos:
            if producto.cantidad <= 5:
                print(producto)
    
    def mostrar_productos(self):
        for producto in self.__productos:
            print(producto)