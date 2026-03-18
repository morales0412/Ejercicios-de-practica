from inventario import Inventario
from producto import Producto

def main():
    inventario = Inventario()
    
    while True:
        print("\nMenu")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Mostrar productos criticos")
        print("4. Calcular valor total")
        print("5. Salir")

        while True:
            try:
                opcion = int(input("Ingrese una opcion: "))
                if opcion not in [1,2,3,4,5]:
                    print("Ingrese un valor valido")
                    continue
                break
            except ValueError:
                print("Ingrese un valor valido")
        if opcion == 1:
            nombre = input("Ingrese el nombre del producto: ").strip()
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            producto = Producto(nombre,precio,cantidad)
            inventario.agregar_producto(producto)
            print("Producto agregado")
        elif opcion == 2:
            inventario.mostrar_productos()
        elif opcion == 3:
            inventario.mostrar_productos_criticos()
        elif opcion == 4:
            valor_total = inventario.calcular_valor_total()
            print(f"El valor total del inventario es: {valor_total}")
        elif opcion == 5:
            print("Saliendo del programa ...")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()