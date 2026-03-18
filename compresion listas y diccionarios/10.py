productos = {"Laptop": 1200, "Mouse": 25, "Monitor": 300, "Cable": 10}
categoria = {producto: ("Caro" if precio >= 100 else "Barato") for producto,precio in productos.items()}
print(categoria)