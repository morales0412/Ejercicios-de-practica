class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, dict):
            raise ValueError("El producto debe ser un diccionario")
        if len(producto) != 3:
            raise ValueError(
                "El producto debe tener 3 elementos: Nombre, precio y categoria"
            )
        self.productos.append(producto)

    def filtrar_categoria(self, categoria):
        if not isinstance(categoria, str):
            raise ValueError("La categoria debe ser una cadena de texto")
        if not self.productos:
            return []
        productos_filtrados = list(
            filter(lambda producto: producto["categoria"] == categoria, self.productos)
        )
        return productos_filtrados

    def aplicar_descuento(self, porcentaje):
        if not isinstance(porcentaje, int):
            raise ValueError("El porcentaje debe ser un numero entero")
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe ser entre 0 y 100")
        if not self.productos:
            return []
        productos_con_descuento = list(
            map(
                lambda producto: {
                    "nombre": producto["nombre"],
                    "precio": round(producto["precio"] * (1 - porcentaje / 100), 2),
                    "categoria": producto["categoria"],
                },
                self.productos,
            )
        )
        return productos_con_descuento

    def __str__(self):
        return f"Tienda: {self.nombre}, Productos: {len(self.productos)}"


tienda = Tienda("MiTienda")

tienda.agregar_producto({"nombre": "camisa", "precio": 50000, "categoria": "ropa"})
tienda.agregar_producto({"nombre": "pantalon", "precio": 80000, "categoria": "ropa"})
tienda.agregar_producto({"nombre": "manzana", "precio": 2000, "categoria": "frutas"})
tienda.agregar_producto({"nombre": "zapatos", "precio": 120000, "categoria": "calzado"})

tienda = Tienda("MiTienda")

tienda.agregar_producto({"nombre": "camisa", "precio": 50000, "categoria": "ropa"})
tienda.agregar_producto({"nombre": "pantalon", "precio": 80000, "categoria": "ropa"})
tienda.agregar_producto({"nombre": "manzana", "precio": 2000, "categoria": "frutas"})
tienda.agregar_producto({"nombre": "zapatos", "precio": 120000, "categoria": "calzado"})

try:
    print(tienda)
    # MiTienda | Productos: 4

    ropa = tienda.filtrar_categoria("ropa")
    print(ropa)
    # [{"nombre": "camisa", ...}, {"nombre": "pantalon", ...}]

    rebajados = tienda.aplicar_descuento(10)
    print(rebajados)
    # [{"nombre": "camisa", "precio": 45000.0, ...}, ...]
except ValueError as e:
    print(f"Error: {e}")
