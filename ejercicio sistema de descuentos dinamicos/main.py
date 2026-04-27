("""Pequeño ejecutable de ejemplo para el sistema de descuentos dinámicos.

Ejecutar: python main.py
""")

def main():
	from modelos.producto import Producto
	from modelos.carrito import Carrito
	from modelos.descuento import FlatDescuento, PercentageDescuento
	from modelos.procesador_descuento import ProcesadorDescuento
	from excepciones.excepciones_descuentos import NegativePriceError

	# Crear productos
	p1 = Producto("Camisa", 50.0, "Ropa", "1234567890123")
	p2 = Producto("Libro", 20.0, "Libros", "1234567890124")
	p3 = Producto("Taza", 8.0, "Hogar", "1234567890125")

	carrito = Carrito()
	carrito.agregar_producto(p1)
	carrito.agregar_producto(p2)
	carrito.agregar_producto(p3)

	print("Productos en el carrito:")
	for prod in carrito._productos:
		print(" -", prod)

	print("\nSimulación de 10% de descuento:")
	for nombre, precio in carrito.simular_descuento(0.1):
		print(f" - {nombre}: {precio:.2f}")

	descuentos = [FlatDescuento(5), PercentageDescuento(0.1)]
	procesador = ProcesadorDescuento(descuentos)

	try:
		total = procesador.procesar_carrito(carrito)
		print(f"\nTotal con descuentos aplicados: {total:.2f}")
		total_con_cupon = procesador.procesar_carrito(carrito, FlatDescuento(3))
		print(f"Total con cupón adicional: {total_con_cupon:.2f}")
	except NegativePriceError as e:
		print("Error al calcular precios:", e.mensaje)


if __name__ == "__main__":
	main()

