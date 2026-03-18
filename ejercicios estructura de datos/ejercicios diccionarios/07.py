productos = ["camisa", "pantalon", "zapatos"]
precios = [40, 60, 85]

catalogo = {}

for producto,precio in zip(productos,precios):
    catalogo[producto] = precio

print(catalogo)