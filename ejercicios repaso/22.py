# gestor de votaciones
from functools import reduce


class VotoInvalidoError(Exception):
    def __init__(self, candidato):
        self.candidato = candidato
        mensaje = (
            f"El candidato {self.candidato} no se encuentra en la lista de candidatos."
        )
        super().__init__(mensaje)


class Votacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.candidatos = []
        self.votos = {}

    def agregar_candidato(self, nombre_candidato):
        if nombre_candidato in self.candidatos:
            print(f"El candidato {nombre_candidato} ya esta en la lista")
            return
        self.candidatos.append(nombre_candidato)

    def registrar_voto(self, nombre_candidato):
        if not self.candidatos:
            raise ValueError(" No hay candidatos registrados en la votacion.")
        if nombre_candidato not in self.candidatos:
            raise VotoInvalidoError(nombre_candidato)
        self.votos[nombre_candidato] = self.votos.get(nombre_candidato, 0) + 1
        print(f"Voto registrado para {nombre_candidato}")

    def resultados(self):
        if not self.votos:
            print("No se han registrado votos.")
            return
        print(f"Resultados de la votacion {self.nombre}: ")
        resultado = sorted(self.votos.items(), key=lambda x: x[1], reverse=True)
        for candidato, votos in resultado:
            print(f"{candidato}: {votos} votos")

    def ganador(self):
        if not self.votos:
            print("No se han registrado votos.")
            return
        ganador = reduce(lambda x, y: x if x[1] > y[1] else y, self.votos.items())
        print(
            f"El ganador de la votacion {self.nombre} es: {ganador[0]} con {ganador[1]} votos"
        )

    def porcentaje_votos(self):
        if not self.votos:
            print("No se han registrado votos.")
            return
        total_votos = sum(self.votos.values())
        porcentajes = {
            candidato: (votos / total_votos) * 100
            for candidato, votos in self.votos.items()
        }
        return porcentajes


votacion = Votacion("Elecciones 2024")

while True:
    print("\nOpciones:")
    print("1. Agregar candidato")
    print("2. Registrar voto")
    print("3. Mostrar resultados")
    print("4. Mostrar ganador")
    print("5. Mostrar porcentaje de votos")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre_candidato = input("Ingrese el nombre del candidato: ")
        votacion.agregar_candidato(nombre_candidato)
    elif opcion == "2":
        nombre_candidato = input("Ingrese el nombre del candidato al que desea votar: ")
        try:
            votacion.registrar_voto(nombre_candidato)
        except VotoInvalidoError as e:
            print(e)
        except ValueError as e:
            print(e)
    elif opcion == "3":
        votacion.resultados()
    elif opcion == "4":
        votacion.ganador()
    elif opcion == "5":
        porcentajes = votacion.porcentaje_votos()
        if porcentajes:
            for candidato, porcentaje in porcentajes.items():
                print(f"{candidato}: {porcentaje:.2f}% de los votos")
    elif opcion == "6":
        break
    else:
        print("Opcion invalida, por favor intente de nuevo.")
