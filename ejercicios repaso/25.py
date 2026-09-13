# Sistema de biblioteca
from functools import reduce


class LibroNoDisponibleError(Exception):
    def __init__(self, libro):
        self.libro = libro
        self.mensaje = f"El libro '{libro.titulo}' no está disponible para préstamo."
        super().__init__(self.mensaje)


class IsbnInvalidoError(Exception):
    def __init__(self, isbn):
        self.isbn = isbn
        self.mensaje = f"El ISBN '{isbn}' no es válido ( igual a 10 caracteres)."
        super().__init__(self.mensaje)


class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.prestamos = 0

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, valor):
        if len(valor) != 10:
            raise IsbnInvalidoError(valor)
        self._isbn = valor

    def prestar(self):
        if not self.disponible:
            raise LibroNoDisponibleError(self.titulo)
        self.disponible = False
        self.prestamos += 1

    def devolver(self):
        if self.disponible:
            print(f"El libro '{self.titulo}' ya está disponible.")
            return
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} - autor: {self.autor} - ISBN: {self.isbn} - Disponible:: {'Si' if self.disponible else 'No'}"


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro_por_autor(self, autor) -> list[Libro]:
        if not self.libros:
            raise ValueError("No hay libros registrados en la biblioteca. ")
        libros_encontrados = [
            libro for libro in self.libros if libro.autor.lower().strip() == autor
        ]
        return libros_encontrados

    def libros_disponibles(self) -> list[Libro]:
        if not self.libros:
            raise ValueError("No hay libros registrados en la biblioteca.")
        libros_disponibles = [libro for libro in self.libros if libro.disponible]
        return libros_disponibles

    def libro_mas_prestados(self) -> Libro:
        if not self.libros:
            raise ValueError("No hay libros registrados en la biblioteca.")
        libro_mas_prestado = reduce(
            lambda x, y: x if x.prestamos > y.prestamos else y, self.libros
        )
        return libro_mas_prestado

    def autor_mas_libros(self) -> str:
        if not self.libros:
            raise ValueError("No hay libros registrados en la biblioteca.")
        autores = {}
        for libro in self.libros:
            autores[libro.autor] = autores.get(libro.autor, 0) + 1
        autor_mas_libros = max(autores, key=autores.get)
        return autor_mas_libros

    def reporte(self) -> dict:
        if not self.libros:
            raise ValueError("No hay libros registrados en la biblioteca.")
        reporte = {
            "total_libros": len(self.libros),
            "disponibles": [libro.titulo for libro in self.libros if libro.disponible],
            "no_disponibles": [
                libro.titulo for libro in self.libros if not libro.disponible
            ],
            "autor_mas_libros": self.autor_mas_libros(),
        }

        return reporte

    def mostrar_libros(self):
        if not self.libros:
            raise ValueError("No hay libros registrados en la biblioteca. ")
        for libro in self.libros:
            print(libro)


biblioteca = Biblioteca("Biblioteca Central")


def menu():
    print("\n--- Sistema de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Buscar libro por autor")
    print("3. Mostrar libros disponibles")
    print("4. Mostrar libro más prestado")
    print("5. Mostrar autor con más libros")
    print("6. Mostrar reporte de la biblioteca")
    print("7. Salir")


while True:
    menu()
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        isbn = input("Ingrese el ISBN del libro (max 10 caracteres): ")
        try:
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar_libro(libro)
            print(f"Libro '{titulo}' agregado a la biblioteca.")
        except IsbnInvalidoError as e:
            print(e)
    elif opcion == "2":
        biblioteca.mostrar_libros()
        autor = input("Ingrese el autor del libro que desea buscar: ").lower().strip()
        try:
            libros_encontrados = biblioteca.buscar_libro_por_autor(autor)
            if libros_encontrados:
                print(f"Libros encontrados del autor '{autor}':")
                for libro in libros_encontrados:
                    print(libro)
            else:
                print(f"No se encontraron libros del autor '{autor}'. ")
        except ValueError as e:
            print(e)
            print(f"No se encontraron libros del autor '{autor}'. ")

    elif opcion == "3":
        try:
            libros_disponibles = biblioteca.libros_disponibles()
            if libros_disponibles:
                print("Libros disponibles: ")
                for libro in libros_disponibles:
                    print(libro)
            else:
                print("No hay libros disponibles en la biblioteca.")
        except ValueError as e:
            print(e)
    elif opcion == "4":
        try:
            libro_mas_prestado = biblioteca.libro_mas_prestados()
            print(f"El libro más prestado es: {libro_mas_prestado}")
        except ValueError as e:
            print(e)
    elif opcion == "5":
        try:
            autor_mas_libros = biblioteca.autor_mas_libros()
            print(f"El autor con más libros es: {autor_mas_libros}")
        except ValueError as e:
            print(e)
    elif opcion == "6":
        try:
            reporte = biblioteca.reporte()
            print("Reporte de la biblioteca:")
            print(f"Total de libros: {reporte['total_libros']}")
            print(f"Libros disponibles: {', '.join(reporte['disponibles'])}")
            print(f"Libros no disponibles: {', '.join(reporte['no_disponibles'])}")
            print(f"Autor con más libros: {reporte['autor_mas_libros']}")
        except ValueError as e:
            print(e)
    elif opcion == "7":
        print("Saliendo del sistema de biblioteca.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
