from abc import ABC, abstractmethod


class Tarea(ABC):
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.completada = False

    @property
    def prioridad(self):
        return self._prioridad

    @prioridad.setter
    def prioridad(self, valor):
        prioridades_validas = ["alta", "media", "baja"]
        if valor not in prioridades_validas:
            raise ValueError(f"Prioridades validas: {', '.join(prioridades_validas)}")
        self._prioridad = valor

    @abstractmethod
    def ejecutar(self):
        pass


class TareaSimple(Tarea):
    def ejecutar(self):
        self.completada = True
        print(f"Tarea '{self.nombre}' completada.")


class TareaRecurrente(Tarea):
    def __init__(self, nombre, prioridad, repeticiones):
        super().__init__(nombre, prioridad)
        self.repeticiones = repeticiones

    def ejecutar(self):
        if self.completada:
            raise ValueError(f"Tarea recurrente '{self.nombre} ya ha sido completada.")

        if self.repeticiones == 0:
            print(f"Tarea recurrente '{self.nombre}' completada.")
            self.completada = True
        else:
            self.repeticiones -= 1
            print(
                f"Tarea recurrente '{self.nombre}' ejecutada. Repeticiones restantes: {self.repeticiones}"
            )


while True:
    print("\nOpciones:")
    print("1. Crear tarea simple")
    print("2. Crear tarea recurrente")
    print("3. Ejecutar tarea")
    print("4. Filtrar ")
