from .user import User


class Librarian(User):
    def __init__(self, id_usuario: str, nombre: str):
        super().__init__(id_usuario, nombre, "activo")

    def max_prestamos(self):
        return 999999

    def duracion_prestamo(self):
        return 30

    def max_retrasos_permitidos(self):
        return 999999

    def puede_renovar(self):
        return True
