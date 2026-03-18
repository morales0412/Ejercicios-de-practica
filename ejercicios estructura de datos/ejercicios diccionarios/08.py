catalogo = {'camisa': 40, 'pantalon': 60, 'zapatos': 85}

precios_por_producto = {precio: producto for producto,precio in catalogo.items()}
print(precios_por_producto)
