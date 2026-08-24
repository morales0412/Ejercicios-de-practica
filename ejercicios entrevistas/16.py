class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_actual, monto_requerido):
        self.saldo_actual = saldo_actual
        self.monto_requerido = monto_requerido
        faltante = self.monto_requerido - self.saldo_actual
        mensaje = f"Te faltan ${faltante} para realizar la compra"
        super().__init__(mensaje)


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("El saldo debe ser un numero")
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar deber ser positivo")
        self.saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar deber ser positivo")
        if monto > self.saldo:
            raise SaldoInsuficienteError(self.saldo, monto)

        self.saldo -= monto

    def transferir(self, monto, cuenta_destino):
        if not isinstance(cuenta_destino, CuentaBancaria):
            raise ValueError(
                "La cuenta destino debe ser una instancia de CuentaBancaria"
            )
        if monto <= 0:
            raise ValueError("El monto a transferir debe ser positivo")
        if monto > self.saldo:
            raise SaldoInsuficienteError(self.saldo, monto)
        self.retirar(monto)
        cuenta_destino.depositar(monto)
        print(f"Se han transferido ${monto} a la cuenta de {cuenta_destino}")

    def __str__(self):
        return f"Cuenta bancaria de {self.titular} - Saldo: ${self.saldo}"


cuenta1 = CuentaBancaria("Ana", 1000000)
cuenta2 = CuentaBancaria("Luis", 500000)

cuenta1.depositar(500000)
print(cuenta1.saldo)  # 1500000

try:
    cuenta1.retirar(2000000)
except SaldoInsuficienteError as e:
    print(
        e
    )  # SaldoInsuficienteError: Ana no tiene suficiente saldo. Saldo actual: $1500000, intentó retirar: $2000000

cuenta1.transferir(300000, cuenta2)
print(cuenta1.saldo)  # 1200000
print(cuenta2.saldo)  # 800000
