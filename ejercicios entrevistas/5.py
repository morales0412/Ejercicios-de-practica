class CuentaBancaria:
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


cuenta = CuentaBancaria("Ana", 100000)
cuenta.depositar(50000)
cuenta.retirar(30000)
cuenta.ver_saldo()
# Saldo actual de Ana: $120000
print(cuenta)
# CuentaBancaria | Titular: Ana | Saldo: $120000
