from .base import AccionInvalidaError


class ErrorEquipamiento(AccionInvalidaError):
    pass


class LimiteEquipamientoError(ErrorEquipamiento):
    def __init__(self, item_nombre):
        self.limite = 6
        self.item_nombre = item_nombre
        mensaje = f"No se puede equipar '{item_nombre}'. El limite de items equipados es {self.limite}."
        super().__init__(mensaje)
