from empleado import Empleado

class EmpleadoComision(Empleado):
    
    def __init__(self,nombre,id,ventas_realizadas,porcentaje_comision):
        super().__init__(nombre,id)
        self.ventas_realizadas = ventas_realizadas
        self.procentaje_comision = porcentaje_comision

    def calcular_salario(self):
        return self.ventas_realizadas * self.procentaje_comision
