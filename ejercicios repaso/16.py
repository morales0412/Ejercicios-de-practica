class Producto:
    categorias = ["ropa", "calzado", "electronica", "alimentos"]

    def __init__(self, nombre, precio, descuento, categoria):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
        self.categoria = categoria

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacio.")
        if len(valor) > 50:
            raise ValueError(
                "El nombre del producto no puede tener mas de 50 caracteres."
            )
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("El precio debe ser un numero.")
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, valor):
        if valor < 0 or valor > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        self._descuento = valor

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        valor = valor.lower().strip()
        if valor not in self.categorias:
            raise ValueError(f"Categorias validas: {', '.join(self.categorias)}")
        self._categoria = valor

    @property
    def precio_final(self):
        return self.precio * (1 - self.descuento / 100)

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio} | Descuento: {self.descuento}% | Categoria: {self.categoria} | Precio Final: {self.precio_final}"
