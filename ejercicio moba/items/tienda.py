from copy import deepcopy

from excepciones.excepcion_recursos import OroInsuficienteError
from items.item import Item


class Tienda:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def items_para_tipo(self, tipo_personaje):
        return self.catalogo.get(tipo_personaje, []) + self.catalogo.get("Comunes", [])

    def mostrar(self, tipo_personaje, salida=print):
        items = self.items_para_tipo(tipo_personaje)
        salida("\n=== TIENDA ===")
        for indice, item in enumerate(items, start=1):
            salida(f"{indice}. {item}")
        salida("0. Salir de la tienda")

    def comprar(self, personaje, indice):
        items = self.items_para_tipo(personaje.tipo)
        if indice < 1 or indice > len(items):
            raise ValueError("Item fuera de rango.")

        item_original = items[indice - 1]
        if personaje.oro < item_original.precio:
            raise OroInsuficienteError(personaje.oro, item_original.precio)

        item = Item(
            item_original.nombre,
            item_original.tipo,
            item_original.precio,
            deepcopy(item_original.bonificaciones),
        )

        personaje.equipar_item(item)
        personaje.oro -= item.precio
        return item
