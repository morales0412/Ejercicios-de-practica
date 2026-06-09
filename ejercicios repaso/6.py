class Empleado:
    """
    Clase que tiene 2 metodos de clase cantidad de empleados y aumento general que se le aplica al salario del empleado
    """

    cantidad_empleados = 0
    aumento_general = 0.10

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.cantidad_empleados += 1

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        # Validacion para asegurarse de que el salario sea un numero positivo
        if not isinstance(valor, (int, float)):
            raise ValueError("El salario debe ser un numero.")
        if valor < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salario = valor

    @classmethod
    def obtener_cantidad_empleados(cls):
        # Devuelve la cantidad de empleados creados
        return cls.cantidad_empleados

    @classmethod
    def cambiar_aumento_general(cls, nuevo_aumento):
        # Cambia el aumento general que se le aplica al salario de los empleados
        if not isinstance(nuevo_aumento, (int, float)):
            raise ValueError("El aumento general debe ser un numero.")
        if nuevo_aumento < 0 or nuevo_aumento > 1:
            raise ValueError("El aumento general debe ser entre 0 y 1.")
        cls.aumento_general = nuevo_aumento

    @staticmethod
    def es_salario_valido(salario):
        # Valida si el salario es un numero positivo
        return isinstance(salario, (int, float)) and salario >= 0

    def aplicar_aumento(self):
        self.salario += self.salario * Empleado.aumento_general

    def __str__(self):
        return f"Empleado | Nombre: {self.nombre} | Salario: ${self.aplicar_aumento()}"
