class Producto:
    total_productos = 0
    umbral_premium = 1000

    def __init__(self,nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
        Producto.total_productos += 1
    
    def es_premium(self) -> bool:
        return self.precio >= Producto.umbral_premium
    @classmethod
    def obtener_total_creados (cls) -> int:
        return cls.total_productos

    @classmethod
    def cambiar_umbral_premium(cls,nuevo_umbral: float) -> None:
        cls.umbral_premium = nuevo_umbral