from .personaje import Personaje


class Tanque(Personaje):
    def __init__(self, nombre, stats):
        super().__init__(nombre, "Tanque", stats)

    def aumentar_stats_nivel(self):
        self.stats["vida"] += 100
        self.stats["mana"] += 20
        self.stats["daño_fisico"] += 8
        self.stats["daño_magico"] += 5
        self.stats["resistencia_fisica"] += 15
        self.stats["resistencia_magica"] += 10
