from abc import ABC, abstractmethod


from excepciones.error_equipamiento import (
    LimiteEquipamientoError,
    ItemNoEncontradoError,
)


class Personaje(ABC):
    def __init__(self, nombre, tipo, stats):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.experiencia = 0
        self.oro = 0
        self.stats = stats
        self.mana_actual = self.stats["mana"]
        self.vida_actual = self.stats["vida"]
        self.habilidades = []
        self.items = []

    def recibir_daño(self, cantidad, tipo_daño):
        if tipo_daño == "fisico":
            resistencia = self.stats.get("resistencia_fisica", 0)
        elif tipo_daño == "magico":
            resistencia = self.stats.get("resistencia_magica", 0)
        daño_reducido = cantidad - (cantidad * resistencia / 100)
        self.vida_actual -= max(daño_reducido, 0)
        if self.vida_actual < 0:
            self.vida_actual = 0

    def atacar(self, objetivo, habilidad):
        daño, tipo_daño = habilidad.usar(self)
        objetivo.recibir_daño(daño, tipo_daño)

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        while self.verificar_subida_nivel():
            self.subir_nivel()

    def verificar_subida_nivel(self):
        experiencia_requerida = self.nivel * 100
        return self.experiencia >= experiencia_requerida

    def subir_nivel(self):
        experiencia_requerida = self.nivel * 100
        self.experiencia -= experiencia_requerida
        self.nivel += 1
        self.aumentar_stats_nivel()
        self.vida_actual = self.stats["vida"]
        self.mana_actual = self.stats["mana"]

    @abstractmethod
    def aumentar_stats_nivel(self):
        pass

    def equipar_item(self, item):
        if len(self.items) >= 6:
            raise LimiteEquipamientoError(item.nombre)
        self.items.append(item)
        self.sumar_stats_item(item.stats)

        if self.vida_actual > self.stats["vida"]:
            self.vida_actual = self.stats["vida"]

        if self.mana_actual > self.stats["mana"]:
            self.mana_actual = self.stats["mana"]

    def sumar_stats_item(self, stats_item):
        for stat_item, valor_item in stats_item.items():
            if stat_item in self.stats:
                self.stats[stat_item] += valor_item

    def desequipar_item(self, item_nombre):
        item = next((item for item in self.items if item.nombre == item_nombre), None)
        if not item:
            raise ItemNoEncontradoError(item_nombre)
        self.items.remove(item)
        self.quitar_stats_item(item.stats)

        if self.vida_actual > self.stats["vida"]:
            self.vida_actual = self.stats["vida"]

        if self.mana_actual > self.stats["mana"]:
            self.mana_actual = self.stats["mana"]

    def quitar_stats_item(self, stats_item):
        for stat_item, valor_item in stats_item.items():
            if stat_item in self.stats:
                self.stats[stat_item] -= valor_item

    def __str__(self):
        return f"{self.nombre} (Nivel {self.nivel} {self.tipo}) - Vida: {self.vida_actual}/{self.stats['vida']}, Mana: {self.mana_actual}/{self.stats['mana']}"
