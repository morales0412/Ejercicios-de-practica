from .base import LibraryError


class PermissionError(LibraryError):
    pass


class PermissionDeniedError(PermissionError):
    def __init__(self, id_usuario: str):
        self.id_usuario = id_usuario
        super().__init__(
            f"El usuario {self.id_usuario} no tiene permiso para realizar esta accion"
        )


class OperationNotAllowedError(PermissionError):
    def __init__(self, id_usuario: str):
        self.id_usuario = id_usuario
        super().__init__(
            f"El usuario {self.id_usuario} no tiene permitido esta accion por su rol"
        )
