from .base import AccionInvalidaError


class RestrinccionEstadoError(AccionInvalidaError):
    pass


class PersonajeAturdidoError(RestrinccionEstadoError):
    def __init__(self, nombre_personaje):
        self.nombre_personaje = nombre_personaje
        mensaje = (
            f"{self.nombre_personaje} esta aturdido y no puede realizar esta accion"
        )
        super().__init__(mensaje)


class HechizosSilenciadoError(RestrinccionEstadoError):
    def __init__(self, nombre_personaje):
        self.nombre_personaje = nombre_personaje
        mensaje = f"{self.nombre_personaje} esta silenciado y no puede lanzar hechizos"
        super().__init__(mensaje)
