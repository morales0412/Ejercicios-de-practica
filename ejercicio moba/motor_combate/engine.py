import random

from excepciones.error_equipamiento import LimiteEquipamientoError
from excepciones.excepcion_habilidades import (
    HabilidadBloqueadaError,
    HabilidadEnCooldownError,
)
from excepciones.excepcion_recursos import ManaInsuficienteError


class MotorCombate:
    def __init__(self, lista_personajes):
        self.lista_personajes = lista_personajes

    def elegir_enemigo(self, personaje_escogido):
        enemigos_disponibles = [
            personaje
            for personaje in self.lista_personajes
            if personaje is not personaje_escogido
            and personaje.nombre != personaje_escogido.nombre
        ]
        if not enemigos_disponibles:
            raise ValueError("No hay enemigos disponibles para combatir.")
        return random.choice(enemigos_disponibles)

    def habilidades_usables(self, personaje):
        habilidades_usables = []
        for habilidad in personaje.habilidades:
            try:
                habilidad.puede_usar(personaje)
            except (
                HabilidadBloqueadaError,
                HabilidadEnCooldownError,
                ManaInsuficienteError,
            ):
                continue
            habilidades_usables.append(habilidad)
        return habilidades_usables

    def estado_habilidad(self, personaje, habilidad):
        try:
            habilidad.puede_usar(personaje)
        except (
            HabilidadBloqueadaError,
            HabilidadEnCooldownError,
            ManaInsuficienteError,
        ) as error:
            return f"no disponible ({error})"
        return "lista"

    def elegir_habilidad_aleatoria(self, personaje):
        habilidades_usables = self.habilidades_usables(personaje)
        if habilidades_usables:
            return random.choice(habilidades_usables)
        return None

    def elegir_habilidad_jugador(self, personaje, entrada=input, salida=print):
        while True:
            salida(f"\nTurno de {personaje.nombre} ({personaje.tipo})")
            salida(
                f"Vida: {personaje.vida_actual}/{personaje.stats['vida']} | Mana: {personaje.mana_actual}/{personaje.stats['mana']}"
            )
            salida("Habilidades disponibles:")
            for indice, habilidad in enumerate(personaje.habilidades, start=1):
                salida(
                    f"  {indice}. {habilidad.nombre} - {self.estado_habilidad(personaje, habilidad)}"
                )
            salida("  0. Ataque basico")

            opcion = entrada("Elige una habilidad: ").strip()
            if opcion == "0":
                return None
            if not opcion.isdigit():
                salida("Opcion invalida. Intenta otra vez.")
                continue

            indice = int(opcion)
            if indice < 1 or indice > len(personaje.habilidades):
                salida("Opcion fuera de rango. Intenta otra vez.")
                continue

            habilidad = personaje.habilidades[indice - 1]
            try:
                habilidad.puede_usar(personaje)
            except (
                HabilidadBloqueadaError,
                HabilidadEnCooldownError,
                ManaInsuficienteError,
            ) as error:
                salida(str(error))
                continue
            return habilidad

    def elegir_habilidad_enemigo(self, enemigo):
        return self.elegir_habilidad_aleatoria(enemigo)

    def ataque_basico(self, atacante, defensor, salida=print):
        daño_base = max(
            1, round(atacante.stats.get("daño_fisico", 0) * 0.35 + atacante.nivel * 2)
        )
        defensor.recibir_daño(daño_base, "fisico")
        salida(
            f"{atacante.nombre} ejecuta un ataque basico e inflige {daño_base} de daño fisico a {defensor.nombre}."
        )
        salida(
            f"{defensor.nombre} queda con {defensor.vida_actual}/{defensor.stats['vida']} de vida."
        )

    def ejecutar_ataque(self, atacante, defensor, habilidad=None, salida=print):
        if habilidad is None:
            self.ataque_basico(atacante, defensor, salida=salida)
            return None

        atacante.atacar(defensor, habilidad)
        salida(f"{atacante.nombre} usa {habilidad.nombre} contra {defensor.nombre}.")
        salida(
            f"{defensor.nombre} queda con {defensor.vida_actual}/{defensor.stats['vida']} de vida."
        )
        return habilidad

    def reducir_cooldowns(self, personaje):
        for habilidad in personaje.habilidades:
            habilidad.reducir_cooldown()

    def equipar_items(self, personaje, items, salida=print):
        for item in items:
            try:
                personaje.equipar_item(item)
                salida(f"{personaje.nombre} equipa {item.nombre}.")
            except LimiteEquipamientoError as error:
                salida(str(error))

    def batalla(self, personaje_escogido, enemigo=None, entrada=input, salida=print):
        if enemigo is None:
            enemigo = self.elegir_enemigo(personaje_escogido)

        salida("\n=== COMBATE INICIADO ===")
        salida(f"Jugador: {personaje_escogido.nombre} ({personaje_escogido.tipo})")
        salida(f"Enemigo: {enemigo.nombre} ({enemigo.tipo})")

        turno_jugador = random.choice([True, False])
        numero_turno = 1

        while personaje_escogido.vida_actual > 0 and enemigo.vida_actual > 0:
            salida(f"\n--- Turno {numero_turno} ---")
            if turno_jugador:
                habilidad = self.elegir_habilidad_jugador(
                    personaje_escogido, entrada=entrada, salida=salida
                )
                self.ejecutar_ataque(
                    personaje_escogido, enemigo, habilidad=habilidad, salida=salida
                )
                self.reducir_cooldowns(personaje_escogido)
            else:
                habilidad = self.elegir_habilidad_enemigo(enemigo)
                if habilidad is None:
                    salida(
                        f"{enemigo.nombre} no tiene habilidades disponibles y usa ataque basico."
                    )
                self.ejecutar_ataque(
                    enemigo, personaje_escogido, habilidad=habilidad, salida=salida
                )
                self.reducir_cooldowns(enemigo)
            turno_jugador = not turno_jugador
            numero_turno += 1

        ganador = personaje_escogido if personaje_escogido.vida_actual > 0 else enemigo
        perdedor = enemigo if ganador is personaje_escogido else personaje_escogido

        ganador.ganar_experiencia(120)
        ganador.oro += 60

        salida(
            f"\n{ganador.nombre} ({ganador.tipo}) gana la batalla contra {perdedor.nombre}."
        )
        salida("Recompensa: 120 de experiencia y 60 de oro.")
        return ganador
