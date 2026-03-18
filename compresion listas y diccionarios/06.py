precios = [5, 12, 45, 8, 22, 90]
categoria = ["caro" if precio > 20 else "barato" for precio in precios] 
print(categoria)