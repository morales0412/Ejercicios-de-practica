from .base import LibraryError


class UserError(LibraryError):
    pass


class UserSuspendedError(UserError):
    def __init__(self, id_usuario: str):
        self.id_usuario = id_usuario
        super().__init__(f"El usuario {self.id_usuario} esta suspendido.")


class DuplicatedUserError(UserError):
    def __init__(self, id_usuario: str):
        self.id_usuario = id_usuario
        super().__init__(f"El usuario {self.id_usuario} ya existe")


class InvalidUserStateError(UserError):
    def __init__(self, estado: str):
        self.estado = estado
        super().__init__(f"El estado {self.estado} no es valido para el usuario")


class UserNotFoundError(UserError):
    def __init__(self, id_usuario: str):
        self.id_usuario = id_usuario
        super().__init__(f"El usuario {self.id_usuario} no existe")
