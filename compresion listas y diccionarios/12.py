stock = {"pera": 10, "manzana": 5, "uva": 20}
nuevo_stock = {fruta.upper(): cantidad * 2 for fruta,cantidad in stock.items() if cantidad > 7}
print(nuevo_stock)