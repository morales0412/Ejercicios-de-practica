from datetime import datetime, timedelta

from excepciones.loan_exceptions import (
    LoanLimitExceededError,
    LoanExpiredError,
    LoanAlreadyClosedError,
)

from excepciones.user_exceptions import UserSuspendedError
from excepciones.book_exceptions import BookNotAvailableError


class Loan:
    def __init__(self, id_prestamo: str, usuario, libro):
        if usuario.esta_suspendido():
            raise UserSuspendedError(usuario.id_usuario)

        if usuario.cantidad_prestamos_activos() >= usuario.max_prestamos():
            raise LoanLimitExceededError(usuario.id_usuario)

        if not libro.esta_disponible():
            raise BookNotAvailableError(libro.codigo)

        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_inicio = datetime.now()
        self.fecha_fin = self.fecha_inicio + timedelta(days=usuario.duracion_prestamo())
        self.estado = "activo"

        usuario.agregar_prestamo(self)
        libro.marcar_prestado()
        libro.agregar_prestamo(self)

    def esta_activo(self):
        return self.estado == "activo"

    def esta_expirado(self):
        return self.estado == "activo" and datetime.now() > self.fecha_fin

    def cerrar_prestamo(self):
        if self.estado == "cerrado":
            raise LoanAlreadyClosedError(self.id_prestamo)
        if self.esta_expirado():
            self.expirar()

        self.estado = "cerrado"
        self.libro.marcar_disponible()
        self.usuario.cerrar_prestamo(self)

    def expirar(self):
        if self.estado != "activo":
            raise LoanExpiredError(self.id_prestamo)
        self.estado = "expirado"
        self.libro.marcar_disponible()
        self.usuario._retrasos += 1
        if self.usuario._retrasos > self.usuario.max_retrasos_permitidos():
            self.usuario.suspender(7)

    def renovar(self):
        if not self.usuario.puede_renovar():
            raise LoanExpiredError(self.id_prestamo)

        if self.esta_expirado():
            raise LoanExpiredError(self.id_prestamo)

        self.fecha_fin = self.fecha_fin + timedelta(
            days=self.usuario.duracion_prestamo()
        )
