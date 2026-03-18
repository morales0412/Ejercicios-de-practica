precios = [15.5, 10.0, 22.99, 10.0, 5.0, 15.5, 10.0]

for precio in precios:
    if precio  == 10.0:
        print(f"el indice es {precios.index(precio)}")
        break

print(len([x for x in precios if x == 15.0]))