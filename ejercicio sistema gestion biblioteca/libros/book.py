from excepciones.book_exceptions import BookNotAvailableError
from excepciones.book_exceptions import (
    InvalidBookStateError,
    DuplicateBookError,
)


class Book:
    _codigos_registrados = set()
    _contador_libros = 0

    def __init__(self, codigo: str, titulo: str, autor: str, genero: str, estado: str):

        self.validar_codigo(codigo)
        self.validar_estado(codigo, estado)

        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.estado = estado
        self._prestamos = []

        Book._codigos_registrados.add(codigo)
        Book._contador_libros += 1

    @classmethod
    def validar_codigo(cls, codigo: str):
        if codigo in cls._codigos_registrados:
            raise DuplicateBookError(codigo)

    @staticmethod
    def validar_estado(codigo: str, estado: str):
        if estado not in ["disponible", "prestado"]:
            raise InvalidBookStateError(codigo, estado)

    def esta_disponible(self) -> bool:
        return self.estado == "disponible"

    def marcar_prestado(self):
        if not self.esta_disponible():
            raise BookNotAvailableError(self.codigo)
        self.estado = "prestado"

    def marcar_disponible(self):
        self.estado = "disponible"

    def agregar_prestamo(self, prestamo):
        self._prestamos.append(prestamo)
