from abc import ABC, abstractmethod


class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensaje):
        pass


class NotificadorEmail(Notificador):
    def __init__(self, email):
        self.email = email

    def notificar(self, mensaje):
        print(f"Enviando email a {self.email} con el mensaje: {mensaje}")


class SmsNotificador(Notificador):
    def __init__(self, numero):
        self.numero = numero

    def notificar(self, mensaje):
        if len(mensaje) > 50:
            print(f"Enviando SMS a {self.numero} con el mensaje. {mensaje[:50]}...")
        else:
            print(f"Enviando SMS a {self.numero} con el mensaje: {mensaje}")


email = NotificadorEmail()
