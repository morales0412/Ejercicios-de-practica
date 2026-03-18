from .base import LibraryError


class LoanError(LibraryError):
    pass


class LoanLimitExceededError(LoanError):
    def __init__(self, id_usuario: str):
        self.id_usuario = id_usuario
        super().__init__(
            f"El usuario {self.id_usuario} ha excedido el limite de prestamos"
        )


class LoanExpiredError(LoanError):
    def __init__(self, id_prestamo: str):
        self.id_prestamo = id_prestamo
        super().__init__(f"El prestamo {self.id_prestamo} ha expirado")


class LoanAlreadyClosedError(LoanError):
    def __init__(self, id_prestamo: str):
        self.id_prestamo = id_prestamo
        super().__init__(f"El prestamo {self.id_prestamo} ya se encuentra cerrado")


class InvalidLoanOperationError(LoanError):
    def __init__(self, id_prestamo: str):
        self.id_prestamo = id_prestamo
        super().__init__(
            f"La operacion no es valida para el prestamo {self.id_prestamo}"
        )


class LoanNotFoundError(LoanError):
    def __init__(self, id_prestamo=str):
        self.id_prestamo = id_prestamo
        super().__init__(f"El prestamo {self.id_prestamo} no se encuentra")
