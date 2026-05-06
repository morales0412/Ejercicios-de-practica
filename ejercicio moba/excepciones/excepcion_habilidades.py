from .base import AccionInvalidaError


class ErrorHabilidad(AccionInvalidaError):
    pass


class HabilidadEnCooldownError(ErrorHabilidad):
    def __init__(self, habilidad_nombre, cooldown_restante):
        self.habilidad_nombre = habilidad_nombre
        self.cooldwon_restante = cooldown_restante
        mensaje = f"Habilidad '{habilidad_nombre}' en cooldown. Tiempo restante: {cooldown_restante} segundos."
        super().__init__(mensaje)


class HabilidadBloqueadaError(ErrorHabilidad):
    def __init__(self, nivel_requerido):
        self.nivel_requerido = nivel_requerido
        mensaje = f"Se requiere nivel {self.nivel_requerido} para usar esta habilidad."
        super().__init__(mensaje)
