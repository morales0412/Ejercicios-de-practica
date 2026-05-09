from .personaje import Personaje


class Mago(Personaje):
    def __init__(self, nombre, stats):
        super().__init__(nombre, "Mago", stats)

    def aumentar_stats_nivel(self):
        self.stats["vida"] += 20
        self.stats["mana"] += 30
        self.stats["daño_fisico"] += 5
        self.stats["daño_magico"] += 20
        self.stats["resistencia_fisica"] += 6
        self.stats["resistencia_magica"] += 5
