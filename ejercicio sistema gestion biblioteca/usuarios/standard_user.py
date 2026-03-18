from .user import User


class StandardUser(User):
    def __init__(self, id_usuario: str, nombre: str):
        super().__init__(id_usuario, nombre, "activo")

    def max_prestamos(self):
        return 5

    def duracion_prestamo(self):
        return 7

    def max_retrasos_permitidos(self):
        return 1

    def puede_renovar(self):
        return False
