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


tareas = []

while True:
    print("\nOpciones:")
    print("1. Crear tarea simple")
    print("2. Crear tarea recurrente")
    print("3. Ejecutar tarea")
    print("4. Filtrar tareas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre de la tarea: ")
        prioridad = input("Ingrese la prioridad (alta, media, baja): ").lower().strip()
        try:
            tarea = TareaSimple(nombre, prioridad)
            print(f"Tarea simple '{nombre}' creada con prioridad '{prioridad}'.")
            tareas.append(tarea)
        except ValueError as e:
            print(e)
    elif opcion == "2":
        nombre = input("Ingrese el nombre de la tarea: ")
        prioridad = input("Ingrese la prioridad (alta, media, baja): ").lower().strip()
        while True:
            try:
                repeticiones = int(input("Ingrese el numero de repeticiones: "))
                if repeticiones < 0:
                    print("El numero de repeticiones no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un numero valido.")
        try:
            tarea = TareaRecurrente(nombre, prioridad, repeticiones)
            print(
                f"Tarea recurrente '{nombre}' creada con prioridad '{prioridad}' y {repeticiones} repeticiones."
            )
            tareas.append(tarea)
        except ValueError as e:
            print(e)
    elif opcion == "3":
        if not tareas:
            print("No hay tareas registradas.")
            continue
        while True:
            try:
                print("\n--- Tareas registradas ---")
                for i, tarea in enumerate(tareas, start=1):
                    estado = "completada" if tarea.completada else "pendiente"
                    tipo = (
                        "Recurrente" if isinstance(tarea, TareaRecurrente) else "Simple"
                    )
                    print(f"{i}. {tarea.nombre} - {tipo} - {estado}")
                tarea_seleccionada = int(input("Seleccione una tarea por numero: "))
                if tarea_seleccionada < 1 or tarea_seleccionada > len(tareas):
                    print("Ingrese un numero valido.")
                    continue
                tareas[tarea_seleccionada - 1].ejecutar()
                break
            except ValueError:
                print("Por favor, ingrese un numero valido.")
    elif opcion == "4":
        if not tareas:
            print("No hay tareas registradas.")
            continue
        while True:
            try:
                prioridad_filtro = (
                    input("Ingrese la prioridad para filtrar (alta, media, baja): ")
                    .lower()
                    .strip()
                )
                if prioridad_filtro not in ["alta", "media", "baja"]:
                    print("Ingrese una prioridad valida.")
                    continue
                tareas_filtradas = list(
                    filter(lambda tarea: tarea.prioridad == prioridad_filtro, tareas)
                )
                if not tareas_filtradas:
                    print(f"No hay tareas con prioridad '{prioridad_filtro}'.")
                    continue
                print(f"\n--- Tareas con prioridad '{prioridad_filtro}' ---")
                for tarea in tareas_filtradas:
                    estado = "completada" if tarea.completada else "pendiente"
                    tipo = (
                        "Recurrente" if isinstance(tarea, TareaRecurrente) else "Simple"
                    )
                    print(f"{tarea.nombre} - {tipo} - {estado}")
                break
            except ValueError:
                print("Por favor, ingrese datos validos.")
    elif opcion == "5":
        print("Saliendo del programa. ")
        break
    else:
        print("Opcion invalida, por favor intente de nuevo.")
