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

    def __str__(self):
        return f"Libreria: {self.nombre}, cantidad de libros: {len(self.libros)}"


biblioteca = Biblioteca("Biblioteca Central")

biblioteca.agregar_libro(
    {"titulo": "El Quijote", "autor": "Cervantes", "año": 1605, "disponible": True}
)
biblioteca.agregar_libro(
    {
        "titulo": "Cien años de soledad",
        "autor": "García Márquez",
        "año": 1967,
        "disponible": False,
    }
)
biblioteca.agregar_libro(
    {
        "titulo": "El amor en tiempos de cólera",
        "autor": "García Márquez",
        "año": 1985,
        "disponible": True,
    }
)
biblioteca.agregar_libro(
    {"titulo": "1984", "autor": "Orwell", "año": 1949, "disponible": True}
)

print(biblioteca)
# Biblioteca Central | Libros: 4

print(biblioteca.libros_disponibles())
# ["El Quijote", "El amor en tiempos de cólera", "1984"]

print(biblioteca.buscar_por_autor("García Márquez"))
# [{"titulo": "Cien años de soledad", ...}, {"titulo": "El amor en tiempos de cólera", ...}]
