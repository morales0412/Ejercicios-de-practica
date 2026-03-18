from empleado import Empleado

class Gerente(Empleado):
    def __init__ (self,nombre,departamento,salario,equipo_a_cargo):
        super().__init__(nombre,departamento,salario)
        self.__equipo_a_cargo = equipo_a_cargo
    
    def calcular_bonificacion(self):
        return self.salario * 0.2
    
    def __str__(self):
        return f"{super().__str__()}, Equipo a cargo: {self.__equipo_a_cargo} empleados"
    