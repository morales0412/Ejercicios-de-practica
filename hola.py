class personaje:
    def __init__(self, nombre, stats):
        self.nombre = nombre
        self.stats = stats

    def añadir_stats(self, stats_adicionales):
        for stat_item, valor_item in stats_adicionales.items():
            if stat_item in self.stats:
                self.stats[stat_item] += valor_item


personaje1 = personaje("Andres", {"vida": 100, "mana": 50, "fuerza": 20})
item1 = {"vida": 20, "fuerza": 5}
personaje1.añadir_stats(item1)
print(personaje1.stats)
