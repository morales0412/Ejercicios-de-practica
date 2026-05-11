from excepciones.excepcion_habilidades import (
    HabilidadEnCooldownError,
    HabilidadBloqueadaError,
)
from excepciones.excepcion_recursos import ManaInsuficienteError


class Habilidad:
    def __init__(
        self,
        nombre,
        daño_base,
        tipo_daño,
        enfriamiento,
        costo_mana,
        nivel_requerido,
        escalado,
        frase,
    ):
        self.nombre = nombre
        self.daño_base = daño_base
        self.tipo_daño = tipo_daño
        self.enfriamiento = enfriamiento
        self.enfriamiento_actual = 0
        self.costo_mana = costo_mana
        self.nivel_requerido = nivel_requerido
        self.escalado = escalado
        self.frase = frase

    def calcular_daño(self, stats_personaje):
        daño_total = self.daño_base
        for stat, porcentaje in self.escalado.items():
            daño_total += stats_personaje.get(stat, 0) * porcentaje / 100
        return daño_total, self.tipo_daño

    def puede_usar(self, personaje):
        if personaje.nivel < self.nivel_requerido:
            raise HabilidadBloqueadaError(
                self.nombre, self.nivel_requerido, personaje.nivel
            )
        if personaje.mana_actual < self.costo_mana:
            raise ManaInsuficienteError(
                self.nombre, self.costo_mana, personaje.mana_actual
            )
        if self.enfriamiento_actual > 0:
            raise HabilidadEnCooldownError(self.nombre, self.enfriamiento_actual)

    def usar(self, personaje):
        self.puede_usar(personaje)
        personaje.mana_actual -= self.costo_mana
        self.enfriamiento_actual = self.enfriamiento
        print(self.frase)
        daño, tipo_daño = self.calcular_daño(personaje.stats)
        return daño, tipo_daño

    def reducir_cooldown(self):
        if self.enfriamiento_actual > 0:
            self.enfriamiento_actual -= 1

    def __str__(self):
        return f"{self.nombre} (Daño: {self.daño_base}, Tipo: {self.tipo_daño}, Enfriamiento: {self.enfriamiento_actual} turnos, Costo de Mana: {self.costo_mana}, Nivel Requerido: {self.nivel_requerido})"
