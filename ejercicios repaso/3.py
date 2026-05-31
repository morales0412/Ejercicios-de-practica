from functools import reduce

productos = [
    {"nombre": "camisa", "categoria": "ropa"},
    {"nombre": "pantalon", "categoria": "ropa"},
    {"nombre": "manzana", "categoria": "fruta"},
    {"nombre": "zapatos", "categoria": "calzado"},
    {"nombre": "pera", "categoria": "fruta"},
]


def agrupar_por_categoria(productos):
    """
    Agrupa una lista de productos por su categoría usando reduce.

    Args:
        productos (list): Lista de diccionarios con nombre y categoria
    Returns:
        dict: Diccionario agrupado por categoría
    """
    return reduce(
        lambda acc, producto: {
            **acc,
            producto["categoria"]: acc.get(producto["categoria"], [])
            + [producto["nombre"]],
        },
        productos,
        {},
    )


resultado = agrupar_por_categoria(productos)
print(resultado)
