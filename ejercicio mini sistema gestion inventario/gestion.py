class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):

        return f"{self.nombre} - {self.precio}$ - {self.cantidad} unidades"


def actualizacion_stock(inventario, producto, cantidad_vendida):
    for item in inventario:
        if item.nombre == producto.nombre:
            item.cantidad -= cantidad_vendida
            print(f"Stock actualizado para {item.nombre}")


def mostrar_inventario(inventario):
    print("Inventario actual:")
    for producto in inventario:
        print(f"{producto.nombre} - {producto.precio}$ - {producto.cantidad} unidades")


inventario = [
    Producto("Laptop", 1200.00, 10),
    Producto("Smartphone", 800.00, 20),
    Producto("Tablet", 400.00, 15),
    Producto("Monitor", 300.00, 5),
    Producto("Teclado", 50.00, 25),
]

calculo_total = sum(producto.precio * producto.cantidad for producto in inventario)
print(f"Valor total del inventario: {calculo_total} $")

productos_premium = [producto for producto in inventario if producto.precio > 500.00]
print("Productos premium:")

for producto in productos_premium:
    print(producto.nombre)

while True:
    print("Desea actualizar el stock de un producto? (s/n): ")
    respuesta = input().lower().strip()
    if respuesta not in ("s", "n"):
        print("Respuesta no válida. Por favor ingrese 's' o 'n'")
        continue
    if respuesta == "n":
        print("Saliendo del programa.")
        break
    mostrar_inventario(inventario)
    while True:
        nombre_producto = (
            input("Ingrese el nombre del producto a actualizar: ").strip().capitalize()
        )

        if not any(producto.nombre == nombre_producto for producto in inventario):
            print("Producto no encontrado. Por favor intente nuevamente.")
            continue
        cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
        producto = next(
            producto for producto in inventario if producto.nombre == nombre_producto
        )
        if cantidad_vendida > producto.cantidad:
            print("No hay suficiente stock")
        else:
            actualizacion_stock(inventario, producto, cantidad_vendida)
        break
