from tienda.bodega import Bodega
from productos.productos import Producto


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El valor no puede estar vacío.")


def pedir_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")


def pedir_flotante(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número válido.")


def pedir_categoria(mensaje):
    validas = [categoria.lower() for categoria in Producto.categorias_validas]
    while True:
        valor = input(mensaje).strip()
        if valor.lower() in validas:
            return valor.capitalize()
        print("Categoría inválida. Válidas: Smartphone, Laptop, Accesorio.")


def mostrar_productos(bodega):
    if not bodega.inventario:
        print("No hay productos registrados.")
        return

    print("\n--- Productos ---")
    for producto in bodega.inventario.values():
        print(
            f"ID: {producto.id_producto} | Nombre: {producto.nombre} | "
            f"Categoría: {producto.categoria} | Precio: {producto.precio} | Stock: {producto.stock}"
        )


def obtener_producto(bodega):
    if not bodega.inventario:
        print("No hay productos para seleccionar.")
        return None

    mostrar_productos(bodega)
    id_producto = pedir_texto("Ingrese el ID del producto: ")
    producto = bodega.inventario.get(id_producto)
    if producto is None:
        print("No existe un producto con ese ID.")
    return producto


def agregar_producto(bodega):
    print("\n--- Agregar producto ---")
    id_producto = pedir_texto("ID: ")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_categoria("Categoría (Smartphone/Laptop/Accesorio): ")
    precio = pedir_flotante("Precio: ", minimo=0)
    stock = pedir_entero("Stock inicial: ", minimo=0)

    try:
        producto = Producto(id_producto, nombre, categoria, precio, stock)
        bodega.agregar_producto(producto)
        print("Producto agregado correctamente.")
    except Exception as error:
        print(f"No se pudo agregar el producto: {error}")


def vender_producto(bodega):
    print("\n--- Vender producto ---")
    producto = obtener_producto(bodega)
    if producto is None:
        return

    cantidad = pedir_entero("Cantidad a vender: ", minimo=1)

    try:
        bodega.vender_producto(producto.id_producto, cantidad)
        print("Venta realizada correctamente.")
    except Exception as error:
        print(f"No se pudo vender: {error}")


def actualizar_producto(bodega):
    print("\n--- Actualizar producto ---")
    producto = obtener_producto(bodega)
    if producto is None:
        return

    while True:
        print("\n¿Qué deseas actualizar?")
        print("1) Nombre")
        print("2) Categoría")
        print("3) Precio")
        print("4) Stock")
        print("5) Terminar")

        opcion = input("Elija una opción: ").strip()

        try:
            if opcion == "1":
                producto.nombre = pedir_texto("Nuevo nombre: ")
                print("Nombre actualizado.")
            elif opcion == "2":
                producto.categoria = pedir_categoria(
                    "Nueva categoría (Smartphone/Laptop/Accesorio): "
                )
                print("Categoría actualizada.")
            elif opcion == "3":
                producto.precio = pedir_flotante("Nuevo precio: ", minimo=0)
                print("Precio actualizado.")
            elif opcion == "4":
                nuevo_stock = pedir_entero("Nuevo stock total: ", minimo=0)
                diferencia = nuevo_stock - producto.stock
                producto.actualizar_stock(diferencia)
                print("Stock actualizado.")
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")
        except Exception as error:
            print(f"No se pudo actualizar: {error}")


def mostrar_menu():
    print("\n=== Sistema de Stock ===")
    print("1) Añadir producto")
    print("2) Vender producto")
    print("3) Actualizar producto")
    print("4) Mostrar productos")
    print("5) Salir")


def main():
    bodega = Bodega()

    acciones = {
        "1": agregar_producto,
        "2": vender_producto,
        "3": actualizar_producto,
        "4": mostrar_productos,
    }

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()

        if opcion == "5":
            print("Saliendo...")
            break

        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida.")
            continue

        try:
            accion(bodega)
        except Exception as error:
            print(f"Ocurrió un error inesperado: {error}")


if __name__ == "__main__":
    main()
