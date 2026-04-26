from abc import ABC, abstractmethod


class ValidationError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class InsuficcientFundsError(ValidationError):
    def __init__(self, saldo_actual, monto_requerido):
        mensaje = f"Saldo Insuficiente: saldo actual {saldo_actual}, monto requerido {monto_requerido}"
        super().__init__(mensaje)


class AccountStatusError(ValidationError):
    def __init__(self, titular_cuenta):
        mensaje = (
            f"Estado de la cuenta {titular_cuenta} no permite realizar esta operacion"
        )
        super().__init__(mensaje)


class DailyLimitExceededError(ValidationError):
    def __init__(self, titular_cuenta, limite_diario):
        mensaje = f"Limite diario excedido para {titular_cuenta} - limite diario {limite_diario}"
        super().__init__(mensaje)


class ReglaDeNegocio(ABC):
    @abstractmethod
    def validar(self, cuenta, monto):
        pass


class ReglaSaldo(ReglaDeNegocio):
    def validar(self, cuenta, monto):
        if cuenta.saldo < monto:
            raise InsuficcientFundsError(cuenta.saldo, monto)


class ReglaEstado(ReglaDeNegocio):
    def validar(self, cuenta, monto):
        if cuenta.estado != "activa":
            raise AccountStatusError(cuenta.titular)


class Cuenta:
    def __init__(self, titular, saldo, estado="activa"):
        self.titular = titular
        self._saldo = saldo
        self.estado = estado

    @property
    def saldo(self):
        return self._saldo
