from .descuento import Descuento, PercentageDescuento
from excepciones.excepciones_descuentos import NegativePriceError


class ProcesadorDescuento:
    def __init__(self, lista_descuentos):
        for descuento in lista_descuentos:
            if not isinstance(descuento, Descuento):
                raise ValueError(
                    "Todos los elementos de la lista deben ser instancias de la clase Descuento"
                )
        self.lista_descuentos = lista_descuentos

    @classmethod
    def crear_modo_rebaja(cls):
        return cls([PercentageDescuento(0.1)])

    def procesar_carrito(self, carrito, *cupones):
        total_general = 0
        for producto in carrito._productos:
            precio_actual = producto.precio_base
            todas_las_reglas = self.lista_descuentos + list(cupones)

            for regla in todas_las_reglas:
                if not isinstance(regla, Descuento):
                    continue
                try:
                    precio_actual = regla.aplicar_descuento(precio_actual)
                except NegativePriceError as e:
                    print(
                        f"Advertencia omitiendo descuento para {producto.nombre}: {e.mensaje}"
                    )
            total_general += precio_actual
        return total_general
