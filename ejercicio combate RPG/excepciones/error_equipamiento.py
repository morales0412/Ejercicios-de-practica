from .base import AccionInvalidaError


class ErrorEquipamiento(AccionInvalidaError):
    pass


class ArmaRotaError(ErrorEquipamiento):
    def __init__(self, nombre_arma):
        self.nombre_arma = nombre_arma
        mensaje = f"El arma {self.nombre_arma} esta rota y no puede ser equipada"
        super().__init__(mensaje)


class RequisitoNivelError(ErrorEquipamiento):
    def __init__(self, nombre_personaje, nivel_requerido):
        self.nombre_personaje = nombre_personaje
        self.nivel_requerido = nivel_requerido
        mensaje = f"{self.nombre_personaje} no cumple el requisito de nivel {self.nivel_requerido} para equipar este objeto"
        super().__init__(mensaje)
