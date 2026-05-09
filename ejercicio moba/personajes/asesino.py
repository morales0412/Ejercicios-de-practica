from .personaje import Personaje


class Asesino(Personaje):
    def __init__(self, nombre, stats):
        super().__init__(nombre, "Asesino", stats)

    def aumentar_stats_nivel(self):
        self.stats["vida"] += 60
        self.stats["mana"] += 10
        self.stats["daño_fisico"] += 20
        self.stats["daño_magico"] += 5
        self.stats["resistencia_fisica"] += 7
        self.stats["resistencia_magica"] += 6
