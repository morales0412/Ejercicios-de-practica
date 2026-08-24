from functools import reduce


class CalificacionError(Exception):
    def __init__(self, nombre_estudiante):
        self.estudiante = nombre_estudiante
        mensaje = f"El estudiante {self.estudiante} tiene un error en la calificacion"
        super().__init__(mensaje)


class MateriaError(Exception):
    def __init__(self, materia):
        self.materia = materia
        mensaje = f"La materia {self.materia} no tiene calificaciones registradas"
        super().__init__(mensaje)


class Estudiante:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.calificaciones = {}

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre del estudiante no puede estar vacio.")

        if len(valor) > 50:
            raise ValueError(
                "El nombre del estudiante no puede tener mas de 50 caracteres."
            )
        self._nombre = valor

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El codigo del estudiante debe ser una cadena de texto.")

        if len(valor) != 8:
            raise ValueError("El codigo del estudiante debe tener 8 caracteres.")

        self._codigo = valor

    def agregar_nota(self, materia, nota):
        if not isinstance(nota, (int, float)):
            raise ValueError("La nota debe ser un numero")

        if nota < 0 or nota > 5:
            raise CalificacionError(self.nombre)

        if materia not in self.calificaciones:
            self.calificaciones[materia] = []

        self.calificaciones[materia].append(nota)

    def promedio_materia(self, materia):
        if not self.calificaciones:
            raise ValueError("El estudiante no tiene calificaciones registradas")

        if materia not in self.calificaciones:
            raise MateriaError(materia)

        return round(
            sum(self.calificaciones[materia]) / len(self.calificaciones[materia]), 2
        )

    def promedio_general(self):
        if not self.calificaciones:
            raise ValueError("El estudiante no tiene calificaciones registradas")

        promedio_materia = list(
            map(lambda notas: sum(notas) / len(notas), self.calificaciones.values())
        )
        promedio_general = reduce(lambda x, y: x + y, promedio_materia, 0) / len(
            self.calificaciones
        )
        return round(promedio_general, 2)

    def materias_aprobadas(self):
        if not self.calificaciones:
            raise ValueError("El estudiante no tiene calificaciones registradas")

        aprobadas = list(
            filter(
                lambda materia: (
                    sum(self.calificaciones[materia])
                    / len(self.calificaciones[materia])
                    >= 3
                ),
                self.calificaciones,
            )
        )
        return aprobadas

    def reporte(self):
        if not self.calificaciones:
            raise ValueError("El estudiante no tiene calificaciones registradas")

        lista_materias = []

        for materia in self.calificaciones:
            lista_materias.append(
                {"materia": materia, "promedio": self.promedio_materia(materia)}
            )

        materias_ordenadas = sorted(
            lista_materias, key=lambda materia: materia["promedio"], reverse=True
        )

        reporte = {
            "nombre": self.nombre,
            "codigo": self.codigo,
            "promedio_general": self.promedio_general(),
            "materias": materias_ordenadas,
        }
        return reporte


andres = Estudiante("Andres", "12345678")

try:
    andres.agregar_nota("matematicas", 4)
    andres.agregar_nota("matematicas", 5)
    andres.agregar_nota("historia", 2)
    print(andres.reporte())
    raise CalificacionError("Andres")
except CalificacionError as e:
    print(e)
except MateriaError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
