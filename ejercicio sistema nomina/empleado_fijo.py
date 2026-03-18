from empleado import Empleado

class EmpleadoFijo(Empleado):
    
    def __init__(self,nombre,id, sueldo_mensual):
        super().__init__(nombre,id)
        self.sueldo_mensual = sueldo_mensual

    def calcular_salario(self):
        return self.sueldo_mensual
    