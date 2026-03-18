from empleado import Empleado

class EmpleadoFullTime(Empleado):
    def __init__ (self,id,nombre,correo,salario_mensual):
        super().__init__(id,nombre,correo)
        self.__salario_mensual = salario_mensual
        self.__bonos = []
    
    @property
    def salario_mensual(self):
        return self.__salario_mensual
    
    @salario_mensual.setter
    def salario_mensual(self,nuevo_salario):
        if nuevo_salario > 0:
            self.__salario_mensual = nuevo_salario
        else:
            raise ValueError("El salario debe ser mayor a cero")
    
    @property
    def suma_bonos(self):
        return sum(self.__bonos)
    
    def agregar_bono(self,bono):
        if bono > 0:
            self.__bonos.append(bono)
        else:
            raise ValueError("El bono debe ser mayor a cero")
    
    def calcular_salario(self):
        total_pago = self.__salario_mensual + self.suma_bonos
        self.registrar_pago(total_pago)
        return total_pago
    
    def __str__(self):
        return f"{super().__str__()}, Salario Mensual: {self.__salario_mensual}, Suma bonos: {'No hay bonos' if not self.__bonos else self.suma_bonos}"