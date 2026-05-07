from abc import ABC, abstractmethod


from abc import ABC


class Personaje(ABC):
    def __init__(self, nombre, tipo):

        self.nombre = nombre
        self.tipo = tipo

        self.nivel = 1
        self.experiencia = 0

        self._vida = 0
        self._vida_max = 0

        self._mana = 0
        self._mana_max = 0

        self.daño_fisico = 0
        self.daño_magico = 0

        self.armadura = 0
        self.resistencia_magica = 0

        self.oro = 0
        self.experiencia_al_matarlo = 0

        self.items = []
        self.habilidades = []

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):

        if valor < 0:
            self._vida = 0
        elif valor > self._vida_max:
            self._vida = self._vida_max
        else:
            self._vida = valor

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, valor):
        if valor < 0:
            self._mana = 0
        elif valor > self._mana_max:
            self._mana = self._mana_max
        else:
            self._mana = valor

    def calcular_daño_recibido(self, cantidad, tipo):
        if tipo == "fisico":
            daño_real = max(cantidad - self.armadura, 0)
        elif tipo == "magico":
            daño_real = max(cantidad - self.resistencia_magica, 0)
        self.vida -= daño_real
        return daño_real

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad

    def verificar_subir_nivel(self):
        exp_necesaria = self.nivel * 100
        if self.experiencia >= exp_necesaria:
            return True
        return False

    @abstractmethod
    def subir_nivel(self):
        pass

    def usar_habilidad(self, habilidad):
        if habilidad in self.habilidades:
            if self.mana >= habilidad.costo_mana and habilidad.enfriamiento == 0:
                self.mana -= habilidad.costo_mana
                return True
            return False
