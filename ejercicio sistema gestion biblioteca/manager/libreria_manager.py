from prestamos.loan import Loan

from excepciones.user_exceptions import UserNotFoundError
from excepciones.book_exceptions import BookNotFoundError
from excepciones.loan_exceptions import LoanNotFoundError


class LibreriaManager:
    def __init__(self):
        self._usuarios = {}
        self._libros = {}
        self._prestamos = {}

    def registrar_usuario(self, usuario):
        self._usuarios[usuario.id_usuario] = usuario

    def registrar_libro(self, libro):
        self._libros[libro.codigo] = libro

    def registrar_prestamo(self, prestamo):
        self._prestamos[prestamo.id_prestamo] = prestamo

    def buscar_usuario(self, id_usuario):
        if id_usuario not in self._usuarios:
            raise UserNotFoundError(id_usuario)
        return self._usuarios[id_usuario]

    def buscar_libro(self, codigo):
        if codigo not in self._libros:
            raise BookNotFoundError(codigo)
        return self._libros[codigo]

    def buscar_prestamo(self, id_prestamo):
        if id_prestamo not in self._prestamos:
            raise LoanNotFoundError(id_prestamo)
        return self._prestamos[id_prestamo]

    def crear_prestamo(self, id_prestamo, id_usuario, codigo):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(codigo)
        prestamo = Loan(id_prestamo, usuario, libro)
        self.registrar_prestamo(prestamo)

    def cerrar_prestamo(self, id_prestamo):
        prestamo = self.buscar_prestamo(id_prestamo)
        prestamo.cerrar_prestamo()
        self._prestamos.pop(id_prestamo)

    def renovar_prestamo(self, id_prestamo):
        prestamo = self.buscar_prestamo(id_prestamo)
        prestamo.renovar()

    def expirar_prestamos(self):
        prestamos_a_expirar = list(self._prestamos.values())

        for prestamo in prestamos_a_expirar:
            if prestamo.esta_expirado():
                prestamo.expirar()
                self._prestamos.pop(prestamo.id_prestamo)
