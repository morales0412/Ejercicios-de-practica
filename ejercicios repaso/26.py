class TorneoError(Exception):
    def __init__(self, cap_maxima):
        self.cap_maxima = cap_maxima
        self.mensaje = (
            f"El torneo ha alcanzado su capacidad maxima de {cap_maxima} jugadores."
        )
        super().__init__(self.mensaje)


class Jugador:
    def __init__(self, nombre, edad, puntos=0):
        self.nombre = nombre
        self.edad = edad
        self.puntos = puntos

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor < 16 or valor > 40:
            raise ValueError("La edad del jugador debe estar entre 16 y 40 años.")
        self._edad = valor

    @property
    def puntos(self):
        return self._puntos

    @puntos.setter
    def puntos(self, valor):
        if valor < 0:
            raise ValueError("Los puntos del jugador no pueden ser negativos. ")
        self._puntos = valor

    def agregar_puntos(self, puntos):
        if puntos < 0:
            raise ValueError("Los puntos a agregar no pueden ser negativos.")
        self.puntos += puntos

    def __str__(self):
        return f"{self.nombre} - Edad: {self.edad} - Puntos: {self.puntos}"


class Torneo:
    def __init__(self, nombre, juego, max_jugadores):
        self.nombre = nombre
        self.juego = juego
        self.jugadores = []
        self.max_jugadores = max_jugadores

    @property
    def max_jugadores(self):
        return self._max_jugadores

    @max_jugadores.setter
    def max_jugadores(self, valor):
        if valor <= 0:
            raise ValueError("La capacidad maxima de jugadores debe ser mayor a 0.")
        self._max_jugadores = valor

    def inscribir(self, jugador):
        if len(self.jugadores) >= self.max_jugadores:
            raise TorneoError(self.max_jugadores)
        self.jugadores.append(jugador)

    def clasificacion(self) -> list[Jugador]:
        if not self.jugadores:
            raise ValueError("No hay jugadores inscritos en el torneo.")
        clasificacion = sorted(self.jugadores, key=lambda x: x.puntos, reverse=True)
        return clasificacion

    def jugador_mas_puntos(self) -> Jugador:
        if not self.jugadores:
            raise ValueError("No hay jugadores inscritos en el torneo.")
        jugador_mas_puntos = max(self.jugadores, key=lambda x: x.puntos)
        return jugador_mas_puntos

    def estadisticas(self) -> dict:
        if not self.jugadores:
            raise ValueError("No hay jugadores inscritos en el torneo. ")

        estadisticas = {
            "total_jugadores": len(self.jugadores),
            "promedio_puntos": sum(jugador.puntos for jugador in self.jugadores)
            / len(self.jugadores),
            "jugador_mas_puntos": self.jugador_mas_puntos().nombre,
            "jugador_menos_puntos": min(self.jugadores, key=lambda x: x.puntos).nombre,
        }

        return estadisticas


torneo = Torneo("Torneo de Videojuegos", "FIFA 2024", 5)


def menu():
    print("=== Menú del Torneo ===")
    print("1. Inscribir jugador")
    print("2. Mostrar clasificación")
    print("3. Mostrar estadísticas")
    print("4. Salir")


while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del jugador: ")
        edad = int(input("Ingrese la edad del jugador: "))
        puntos = int(input("Ingrese los puntos del jugador: "))
        try:
            jugador = Jugador(nombre, edad, puntos)
            torneo.inscribir(jugador)
            print(f"Jugador {nombre} inscrito exitosamente.")
        except (ValueError, TorneoError) as e:
            print(f"Error: {e}")
    elif opcion == "2":
        try:
            clasificacion = torneo.clasificacion()
            print("\n=== Clasificación ===")
            for i, jugador in enumerate(clasificacion, start=1):
                print(f"{i}. {jugador.nombre} - Puntos: {jugador.puntos}")
        except ValueError as e:
            print(f"Error: {e}")
    elif opcion == "3":
        try:
            estadisticas = torneo.estadisticas()
            print("\n=== Estadísticas del Torneo ===")
            print(f"Total de jugadores: {estadisticas['total_jugadores']}")
            print(f"Promedio de puntos: {estadisticas['promedio_puntos']:.2f}")
            print(f"Jugador con más puntos: {estadisticas['jugador_mas_puntos']}")
            print(f"Jugador con menos puntos: {estadisticas['jugador_menos_puntos']}")
        except ValueError as e:
            print(f"Error: {e}")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
