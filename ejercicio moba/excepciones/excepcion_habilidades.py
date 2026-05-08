from .base import AccionInvalidaError


class ErrorHabilidad(AccionInvalidaError):
    pass


class HabilidadEnCooldownError(ErrorHabilidad):
    def __init__(self, habilidad_nombre, enfriamiento_base, enfriamiento):
        self.habilidad_nombre = habilidad_nombre
        self.enfriamiento_base = enfriamiento_base
        self.enfriamiento = enfriamiento
        enfriamiento_restante = self.enfriamiento_base - self.enfriamiento
        mensaje = f"Habilidad '{habilidad_nombre}' en cooldown. Turnos restante: {enfriamiento_restante}."
        super().__init__(mensaje)


class HabilidadBloqueadaError(ErrorHabilidad):
    def __init__(self, nivel_requerido):
        self.nivel_requerido = nivel_requerido
        mensaje = f"Se requiere nivel {self.nivel_requerido} para usar esta habilidad."
        super().__init__(mensaje)
