class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria.
    """

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = valor

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError("Fondos insuficientes.")
        self.saldo -= cantidad

    def ver_saldo(self):
        print(f"Saldo actual de {self.titular}: ${self.saldo}")

    def __str__(self):
        return f"Cuenta Bancaria | Titular: {self.titular}  | Saldo: {self.saldo}"


class CuentaAhorros(CuentaBancaria):
    """
    Clase que representa una cuenta de ahorros, hereda de CuentaBancaria.
    """

    def __init__(self, titular, saldo_inicial=0, tasa_interes=0.05):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes

    @property
    def tasa_interes(self):
        return self._tasa_interes

    @tasa_interes.setter
    def tasa_interes(self, valor):
        if valor < 0 or valor > 1:
            raise ValueError("La tasa de interes debe ser entre 0 y 1")
        self._tasa_interes = valor

    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        print(f"Interes aplicado: ${interes:.2f} | Nuevo saldo: ${self.saldo:.2f}")

    def __str__(self):
        return f"Cuenta de Ahorros | Titular: {self.titular}  | Saldo: {self.saldo} | Tasa de Interés: {self.tasa_interes * 100:.1F}%"


cuenta = CuentaAhorros("Luis", 200000, 0.05)
cuenta.aplicar_interes()
cuenta.ver_saldo()
print(cuenta)
