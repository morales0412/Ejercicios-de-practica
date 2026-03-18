inventario = []

def agregar_producto(nombre,precio, cantidad):
    producto = {}
    producto["nombre"] = nombre
    producto["precio"] = precio
    producto["cantidad"] = cantidad
    inventario.append(producto)

def actualizar_stock(nombre_producto, cantidad):
    encontrado = False
    for producto in inventario:
        if producto["nombre"].lower() == nombre_producto.lower():
            encontrado = True
            
            while True:
                respuesta = input("¿Desea sumar o restar stock? (s/r): ").lower().strip()
                if respuesta in ["s", "r"]:
                    break
                print("Ingrese un valor válido")

            if respuesta == "s":
                producto["cantidad"] += cantidad
                print(f"Stock actualizado: {producto['nombre']} = {producto['cantidad']}")
            else:
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f"Stock actualizado: {producto['nombre']} = {producto['cantidad']}")
                else:
                    print("Error: No puede haber stock negativo.")
            break 
    if not encontrado:
        print("El producto no existe en el inventario.")

def calcular_total():
    total = 0
    for producto in inventario:
        total  += producto["precio"] * producto["cantidad"]
    return total

def productos_criticos():
    productos_criticos = []
    for producto in inventario:
        if producto["cantidad"] <= 5:
            productos_criticos.append(producto["nombre"])
    return productos_criticos

def main():
    while True:
        print("\nMenu")
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Calcular total")
        print("4. Productos criticos")
        print("5. Salir")
        while True:
            opcion = int(input("Ingrese una opcion: "))
            if opcion not in [1,2,3,4,5]:
                print("ingrese un valor valido")
                continue
            break
        if opcion == 1:
            nombre = input("Ingrese el nombre del producto:")
            while True:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    if precio < 0:
                        print("Ingrese un valor positivo")
                        continue
                    break
                except ValueError:
                    print("Ingrese un valor valido")
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                    if cantidad < 0:
                        print("Ingrese un valor positivo")
                        continue
                    break
                except ValueError:
                    print("Ingrese un valor valido")
            agregar_producto(nombre,precio,cantidad)
            print("Se ha agregado el producto")
        elif opcion == 2:
            nombre_producto = input("Ingrese el nombre del producto: ")
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto:"))
                    if cantidad < 0:
                        print("Ingrese un valor positivo")
                        continue
                    break
                except ValueError:
                    print("Ingrese un valor valido")
            actualizar_stock(nombre_producto,cantidad)
            print("Stock actualizado")
        elif opcion == 3:
            total = calcular_total()
            print(f"El total del inventario es: {total}")
        elif opcion == 4:
            lista_criticos = productos_criticos()
            print("Productos criticos:")
            for producto in lista_criticos:
                print(producto)
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()