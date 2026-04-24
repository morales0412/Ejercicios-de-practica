class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"{self.nombre} - Promedio: {self.promedio():.2f}"


def mostrar_estudiantes(estudiantes):
    print("Lista de estudiantes:")
    for estudiante in estudiantes:
        print(estudiante)


curso = [
    Estudiante("Andres", [4.5, 3.8, 4.2]),
    Estudiante("Alejandro", [2.5, 3.0, 2.8]),
    Estudiante("Maria", [5.0, 4.8, 4.9]),
    Estudiante("Carlos", [3.1, 2.9, 3.5]),
    Estudiante("Lucia", [2.0, 1.5, 3.0]),
]

aprobados = [estudiante for estudiante in curso if estudiante.promedio() >= 3.0]

if not aprobados:
    print("No hay estudiantes aprobados.")
else:
    print("Estudiantes aprobados:")
    for estudiante in aprobados:
        print(estudiante)

estudiante_a_buscar = (
    input("Ingrese el nombre del estudiante para buscar: ").strip().capitalize()
)

estudiante_encontrado = next(
    (estudiante for estudiante in curso if estudiante.nombre == estudiante_a_buscar),
    None,
)
if estudiante_encontrado is None:
    print(f"Estudiante {estudiante_a_buscar} no encontrado.")
else:
    print("Estudiante encontrado: ")
    print(estudiante_encontrado)
    print("notas: ")
    for i, nota in enumerate(estudiante_encontrado.notas, start=1):
        print(f"Nota {i}: {nota}")


promedio_global = sum(estudiante.promedio() for estudiante in curso) / len(curso)
print(f"Promedio global del curso: {promedio_global:.2f}")
