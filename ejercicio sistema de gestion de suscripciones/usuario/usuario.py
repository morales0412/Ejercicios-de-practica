from excepciones.excepcion_suscripcion import NivelAccesoInvalido


class Usuario:
    def __init__(self, nombre, email, nivel, saldo):
        self._nombre = nombre
        self._email = email
        self.nivel = nivel
        self._saldo = saldo

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nuevo_nivel):
        nivel_formateado = nuevo_nivel.capitalize()
        if nivel_formateado not in ["Basico", "Premium", "Familiar"]:
            raise NivelAccesoInvalido(nuevo_nivel)
        self._nivel = nivel_formateado

    @staticmethod
    def validar_email(email):
        if "@" in email and email.endswith((".com", ".co")):
            return True
        return False

    def __str__(self):
        return f"{self._nombre} - {self._email} - ${self._saldo:.2f}"
