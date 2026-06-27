class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        """ "
        Agrega un libro a la libreria , pero antes verifica si el valor es tipo diccionario y si tiene las llaves requeridas
        """
        if not isinstance(libro, dict):
            raise ValueError("El libro debe ser un diccionario")
        llaves_requeridas = {"titulo", "autor", "año", "disponible"}
        if not llaves_requeridas.issubset(libro.keys()):
            raise ValueError(
                f"El libro debe tener las siguientes llaves: {llaves_requeridas}"
            )
        self.libros.append(libro)

    def libros_disponibles(self):
        """
        Devuelve una lista de los libros que cuya disponibilidad es True
        """
        if not self.libros:
            return []
        libros_disponibles = [
            libro["titulo"] for libro in self.libros if libro["disponible"]
        ]
        return libros_disponibles

    def buscar_por_autor(self, autor):
        """
        Devuelve una lista de los libros que tengan el mismo autor ingresado por el usuario
        """
        if not isinstance(autor, str):
            raise ValueError("El autor debe ser una cadena de texto")

        if not self.libros:
            return []

        libros_por_autor = list(
            filter(lambda libro: libro["autor"] == autor, self.libros)
        )
        return libros_por_autor

    def resumen_por_año(self):
        """
        Devuelve un diccionario donde las llaves son los años y los valores son listas de
        """
        if not self.libros:
            return []

        resumen_año = {}

        for libro in self.libros:
            año = libro["año"]
            if año not in resumen_año:
                resumen_año[año] = []

            resumen_año[año].append(libro["titulo"])
        return resumen_año

    def libros_en_mayuscuslas(self):
        """
        Devuelve una lista de los títulos de los libros en mayúsculas"""
        if not self.libros:
            return []
        return [libro["titulo"].upper() for libro in self.libros]

    def estadisticas(self):
        """
        Devuelve un diccionario con estadísticas de la librería, incluyendo el total de libros,"""
        if not self.libros:
            return {}

        estadisticas = {
            "total_libros": len(self.libros),
            "libros_disponibles": len(self.libros_disponibles()),
            "libros_no_disponibles": len(self.libros) - len(self.libros_disponibles()),
            "autores_unicos": len(set(libro["autor"] for libro in self.libros)),
        }
        return estadisticas

    def __str__(self):
        return f"Libreria: {self.nombre}, cantidad de libros: {len(self.libros)}"
