from excepciones.estado_error import AturdidoError, SilenciadoError
from .item import Item


class entidad:
    def __init__(self, nombre, nivel, hp, mana, estamina, arma_equipada):
        self.nombre = nombre
        self.nivel = nivel
        self.hp = hp
        self.mana = mana
        self.estamina = estamina
        self.aturdido = False
        self.silenciado = False
        self.arma_equipada = arma_equipada

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, valor):
        if valor < 0 or valor > 18:
            raise ValueError("El nivel debe estar entre 0 y 18")
        self._nivel = valor

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, valor):
        if valor < 0 or valor > 100:
            raise ValueError("El hp debe estar entre 0 y 100")
        self._hp = valor

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, valor):
        if valor < 0 or valor > 100:
            raise ValueError("El mana debe estar entre 0 y 100")
        self._mana = valor

    @property
    def estamina(self):
        return self._estamina

    @estamina.setter
    def estamina(self, valor):
        if valor < 0 or valor > 100:
            raise ValueError("La estamina debe estar entre 0 y 100")
        self._estamina = valor

    @property
    def arma_equipada(self):
        return self._arma_equipada

    @arma_equipada.setter
    def arma_equipada(self, valor):
        if not isinstance(valor, Item):
            raise ValueError("El arma equipada debe ser una instancia de Item")
        self._arma_equipada = valor

    def ejecutar_accion(self, habilidad):
        if self.aturdido:
            raise AturdidoError(self.nombre)
        if self.silenciado and habilidad.tipo == "hechizo":
            raise SilenciadoError(self.nombre)
