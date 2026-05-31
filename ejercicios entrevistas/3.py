def transformar_diccionario(productos):
    """
    Transforma una lista de diccionarios , primero filtra los productos que tienen stock y luego devuelve una nueva lista de diccionarios con el nombre del producto en mayusculas y el precio con un descuento del 10%.
    """
    if not isinstance(productos, list):
        raise ValueError("El argumento debe ser una lista")

    tiene_stock = filter(lambda item: item["stock"] > 0, productos)
    resultado = list(
        map(
            lambda item: {
                "nombre": item["nombre"].upper(),
                "precio": round(item["precio"] * 0.9, 2),
            },
            tiene_stock,
        )
    )

    return resultado


productos = [
    {"nombre": "camisa", "precio": 50000, "stock": 3},
    {"nombre": "pantalon", "precio": 80000, "stock": 0},
    {"nombre": "zapatos", "precio": 120000, "stock": 5},
    {"nombre": "sombrero", "precio": 30000, "stock": 0},
    {"nombre": "chaqueta", "precio": 200000, "stock": 2},
]

try:
    resultado = transformar_diccionario(productos)

    for item in resultado:
        print(f"Nombre: {item['nombre']}, Precio con descuento: {item['precio']}")
except ValueError as e:
    print(e)
