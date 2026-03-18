from abc import ABC, abstractmethod
from datetime import datetime, timedelta

from excepciones.user_exceptions import DuplicatedUserError, InvalidUserStateError
from excepciones.loan_exceptions import LoanLimitExceededError


class User(ABC):
    _ids_registrados = set()
    _contador_usuarios = 0

    def __init__(self, id_usuario: str, nombre: str, estado: str):
        self.validar_id(id_usuario)
        self.validar_estado(estado)

        self.id_usuario = id_usuario
        self.nombre = nombre
        self.estado = estado
        self._prestamos_activos = []
        self._historial_prestamos = []
        self._retrasos = 0
        self._suspension_hasta = None

        User._ids_registrados.add(id_usuario)
        User._contador_usuarios += 1

    @classmethod
    def validar_id(cls, id_usuario: str):
        if id_usuario in cls._ids_registrados:
            raise DuplicatedUserError(id_usuario)

    @staticmethod
    def validar_estado(estado: str):
        if estado.lower().strip() not in ["activo", "suspendido"]:
            raise InvalidUserStateError(estado)

    def esta_suspendido(self):
        if self.estado.lower().strip() != "suspendido":
            return False
        if self._suspension_hasta and datetime.now() >= self._suspension_hasta:
            self.activar()
            return False
        return True

    def suspender(self, dias_suspension: int):
        if dias_suspension <= 0:
            raise ValueError("Los dias de suspension deben ser mayores a 0")
        self._suspension_hasta = datetime.now() + timedelta(days=dias_suspension)
        self.estado = "suspendido"

    def activar(self):
        self.estado = "activo"
        self._suspension_hasta = None
        self._retrasos = 0

    def agregar_prestamo(self, prestamo):
        if self.esta_suspendido():
            raise InvalidUserStateError(self.estado)
        if self.cantidad_prestamos_activos() >= self.max_prestamos():
            raise LoanLimitExceededError(self.id_usuario)
        self._prestamos_activos.append(prestamo)
        self._historial_prestamos.append(prestamo)

    def cerrar_prestamo(self, prestamo):
        self._prestamos_activos.remove(prestamo)

    def cantidad_prestamos_activos(self):
        return len(self._prestamos_activos)

    @abstractmethod
    def max_prestamos(self):
        pass

    @abstractmethod
    def duracion_prestamo(self):
        pass

    @abstractmethod
    def max_retrasos_permitidos(self):
        pass

    @abstractmethod
    def puede_renovar(self):
        pass
