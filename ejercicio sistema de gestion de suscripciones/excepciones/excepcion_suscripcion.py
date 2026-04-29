from .base import SuscripcionException


class NivelAccesoInvalido(SuscripcionException):
    def __init__(self, estado):
        self.estado = estado
        mensaje = f"El nivel de acceso {self.estado} no es valido."
        super().__init__(mensaje)


class FondosInsuficienteError(SuscripcionException):
    def __init__(self, fondo_actual, costo_suscripcion):
        self.fondo_actual = fondo_actual
        self.costo_suscripcion = costo_suscripcion
        mensaje = f"Fondos insuficientes tiene: {self.fondo_actual}, costo de suscripcion: {self.costo_suscripcion}"
        super().__init__(mensaje)


class UsuarioNoActivoError(SuscripcionException):
    def __init__(self, usuario):
        self.usuario = usuario
        mensaje = f"El usuario {self.usuario} no tiene una suscripcion activa"
        super().__init__(mensaje)
