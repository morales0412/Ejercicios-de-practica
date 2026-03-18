from empleado import Empleado

class Desarrollador(Empleado):
    def __init__(self,nombre,departamento,salario,lenguaje_principal):
        super().__init__(nombre,departamento,salario)
        self.__lenguaje_principal = lenguaje_principal
    
    def __str__ (self):
        return f"{super().__str__()}, Lenguaje Principal: {self.__lenguaje_principal}"