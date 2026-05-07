from abc import ABC, abstractmethod


from abc import ABC


class Personaje(ABC):
    def __init__(self, nombre, tipo):

        self.nombre = nombre
        self.tipo = tipo

        self.nivel = 1
        self.experiencia = 0

        self._vida_max = 100
        self._vida = 100

        self._mana_max = 50
        self._mana = 50

        self.daño_fisico = 10
        self.daño_magico = 10

        self.armadura = 5
        self.resistencia_magica = 5

        self.oro = 0

        self.items_equipados = []
        self.habilidades = []
