class DiscountError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ExpiredCouponError(DiscountError):
    def __init__(self, nombre_cupon, fecha_expiracion):
        self.nombre_cupon = nombre_cupon
        self.fecha_expiracion = fecha_expiracion
        mensaje = f"El cupon {self.nombre_cupon} ha expirado el {self.fecha_expiracion}"
        super().__init__(mensaje)


class NegativePriceError(DiscountError):
    def __init__(self, valor_calculado):
        self.valor_calculado = valor_calculado
        mensaje = f"El valor final es negativo: {self.valor_calculado}"
        super().__init__(mensaje)


class InvalidCategoryError(DiscountError):
    def __init__(self, categoria, categorias_validas):
        self.categoria = categoria
        self.categorias_validas = categorias_validas
        mensaje = f"La categoria: {self.categoria} no es valida. Categorias validas: {', '.join(self.categorias_validas)}"
        super().__init__(mensaje)
