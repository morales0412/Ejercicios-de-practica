class MotorCombate:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno = 1

    def iniciar_combate(self):
        print(f"Combate iniciado entre {self.jugador1.nombre} y {self.jugador2.nombre}")
        while self.jugador1.vida_actual > 0 and self.jugador2.vida_actual > 0:
            print(f"\nTurno {self.turno}")
            self.mostrar_estado()
            self.turno += 1

    def mostrar_estado(self):
        print(
            f"{self.jugador1.nombre} - Vida: {self.jugador1.vida_actual}, Mana: {self.jugador1.mana_actual}"
        )
        print(
            f"{self.jugador2.nombre} - Vida: {self.jugador2.vida_actual}, Mana: {self.jugador2.mana_actual}"
        )

    def mostrar_habilidades(self, jugador):
        print(f"Habilidades de {jugador.nombre}: ")
        for indx, habilidad in enumerate(jugador.habilidades, start=1):
            print(f"{indx}. {habilidad}")
