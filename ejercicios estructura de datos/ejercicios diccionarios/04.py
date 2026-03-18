precios = {'manzana': 1.5, 'banana': 0.5}

for valor in precios.values():
    print(valor)

for key,value in precios.items():
    print(f"La {key} cuesta {value}")