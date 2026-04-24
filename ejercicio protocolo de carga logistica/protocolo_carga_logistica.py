class Producto:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def __str__(self):
        return f"{self.nombre} - {self.peso} kg"


producto = ["Laptop", "Smartphone", "Tablet", "Monitor", "Teclado"]
peso = [2.5, 0.5, 0.8, 3.0, 0.3]

carga = list(map(lambda p: Producto(p[0], p[1]), zip(producto, peso)))
print(list(zip(producto, peso)))

for i, item in enumerate(carga, start=1):
    print(f"{i}. {item}")

pesados = list(filter(lambda p: p.peso > 7.0, carga))

if not pesados:
    print("No hay productos pesados.")
else:
    print("Productos pesados: ")
    for i, item in enumerate(pesados, start=1):
        print(f"{i}. {item}")

if any(p.peso > 20.0 for p in carga):
    print("Hay productos que superan los 20 kg.")
else:
    print("No hay productos que superen los 20 kg.")

buscador = next((p for p in carga if p.peso < 1.0), None)

if buscador is None:
    print("No se encontro ningun producto liviano.")
else:
    print(f"Producto liviano encontrado: {buscador}")
