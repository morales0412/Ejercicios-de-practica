from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor):
        if valor < 0 and not isinstance(valor, (int, float)):
            raise ValueError("El salario debe ser un numero positivo")
        self._salario_base = valor

    @abstractmethod
    def calcular_pago(self):
        pass

    def __str__(self):
        return f"Empleado: {self.nombre} - $ {self.calcular_pago()}"


class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    @property
    def bono(self):
        return self._bono

    @bono.setter
    def bono(self, valor):
        if valor < 0:
            raise ValueError("El bono debe ser un numero positivo")
        if not isinstance(valor, (int, float)):
            raise ValueError("El bono debe ser un numero")
        self._bono = valor

    def calcular_pago(self):
        return self.salario_base + self.bono

    def __str__(self):
        return f"Gerente: {self.nombre} - $ {self.calcular_pago()}"


class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, comision_ventas):
        super().__init__(nombre, salario_base)
        self.comision_ventas = comision_ventas

    @property
    def comision_ventas(self):
        return self._comision_ventas

    @comision_ventas.setter
    def comision_ventas(self, valor):
        if valor < 0:
            raise ValueError("La comision de ventas debe ser un numero positivo")
        if not isinstance(valor, (int, float)):
            raise ValueError("La comision de ventas debe ser un numero")
        self._comision_ventas = valor

    def calcular_pago(self):
        return self.salario_base + self.comision_ventas

    def __str__(self):
        return f"Vendedor: {self.nombre} - $ {self.calcular_pago()}"


def filtrar_y_calcular(empleados):
    if not isinstance(empleados, list):
        raise ValueError("El argumento debe ser una lista de empleados")
    if not empleados:
        raise ValueError("La lista de empleados no puede estar vacia")
    gerentes = list(filter(lambda empleado: isinstance(empleado, Gerente), empleados))

    pago_gerentes = list(map(lambda gerente: gerente.calcular_pago(), gerentes))
    return pago_gerentes


empleados = [
    Gerente("Ana", 3000000, 500000),
    Vendedor("Luis", 1500000, 800000),
    Gerente("Maria", 3500000, 600000),
    Vendedor("Pedro", 1500000, 400000),
]

try:
    print(filtrar_y_calcular(empleados))
except ValueError as e:
    print(e)
