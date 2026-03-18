precios = {"manzana": 1.5, 
"banana": 0.5, 
"uva": 3.0
}

precio_naranja = precios.get("naranja", "Producto no encontrado")

precios.pop("uva")
print(precio_naranja)
print(precios)

