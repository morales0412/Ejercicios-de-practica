texto = "banana pera manzana banana manzana pera banana"

palabras = texto.split()
print(palabras)

contador = {}
for palabra in palabras:

    contador[palabra] = contador.get(palabra,0) + 1

print(contador)