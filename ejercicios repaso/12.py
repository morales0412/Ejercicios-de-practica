from functools import reduce


class Tienda:
    """Gestiona una tienda con productos y operaciones sobre ellos."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto a la tienda.

        Args:
            producto (dict): Diccionario con nombre, precio y categoria
        """
        if not isinstance(producto, dict):
            raise ValueError("El producto debe ser un diccionario.")
        llaves_requeridas = {"nombre", "precio", "categoria"}
        if not llaves_requeridas.issubset(producto.keys()):
            raise ValueError("El producto debe tener nombre, precio y categoria.")
        self.productos.append(producto)

    def productos_por_categoria(self, categoria):
        """
        Retorna productos filtrados por categoría.

        Args:
            categoria (str): Categoría a filtrar
        Returns:
            list: Lista de productos de esa categoría
        """
        if not isinstance(categoria, str):
            raise ValueError("La categoria debe ser una cadena de texto.")
        if not self.productos:
            return []
        return list(filter(lambda p: p["categoria"] == categoria, self.productos))

    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento a todos los productos.

        Args:
            porcentaje (int | float): Porcentaje de descuento entre 0 y 100
        Returns:
            list: Lista de productos con precio rebajado
        """
        if not isinstance(porcentaje, (int, float)):
            raise ValueError("El porcentaje debe ser un número.")
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100.")
        if not self.productos:
            return []
        return list(
            map(
                lambda p: {
                    "nombre": p["nombre"],
                    "precio": round(p["precio"] * (1 - porcentaje / 100), 2),
                    "categoria": p["categoria"],
                },
                self.productos,
            )
        )

    def producto_mas_caro(self):
        """
        Retorna el producto más caro de la tienda.
        """
        if not self.productos:
            return None
        producto_mas_caro = reduce(
            lambda x, y: x if x["precio"] > y["precio"] else y, self.productos
        )
        return producto_mas_caro

    def resumen_por_categoria(self):
        """
        Retorna un resumen del número de productos por categoría.}
        """
        if not self.productos:
            return {}
        resumen = {}
        for producto in self.productos:
            categoria = producto["categoria"]
            resumen[categoria] = resumen.get(categoria, 0) + 1
        return resumen

    def ordenar_por_precio(self, ascendente=True):
        """
        Ordena los productos por precio.

        Args:
            ascendente (bool): Si True, ordena de menor a mayor precio. Si False, ordena de mayor a menor.

        Returns:
            list: Lista de productos ordenados por precio.
        """
        if not self.productos:
            return []
        return sorted(self.productos, key=lambda p: p["precio"], reverse=not ascendente)

    def __str__(self):
        return f"{self.nombre} | Productos: {len(self.productos)}"
