from excepciones.error_equipamiento import ArmaRotaError, RequisitoNivelError


class Item:
    def __init__(self, nombre, durabilidad, nivel_requerido):
        self.nombre = nombre
        self.durabilidad = durabilidad
        self.nivel_requerido = nivel_requerido

    @property
    def durabilidad(self):
        return self._durabilidad

    @durabilidad.setter
    def durabilidad(self, valor):
        if valor < 0:
            raise ValueError("La durabilidad no puede ser negativa")
        self._durabilidad = valor

    @property
    def nivel_requerido(self):
        return self._nivel_requerido

    @nivel_requerido.setter
    def nivel_requerido(self, valor):
        if valor < 0 or valor > 18:
            raise ValueError("El nivel requerido debe estar entre 0 y 18")
        self._nivel_requerido = valor

    def usar(self):
        if self.durabilidad <= 0:
            raise ArmaRotaError(self.nombre)
        self.durabilidad = max(0, self.durabilidad - 2)

    def verificar_requesito_nivel(self, personaje):
        if personaje.nivel < self.nivel_requerido:
            raise RequisitoNivelError(personaje.nombre, self.nivel_requerido)

    def __str__(self):
        return f"{self.nombre} - Durabilidad: {self.durabilidad}, Nivel Requerido: {self.nivel_requerido}"
