from empleado import Empleado

class EmpleadoFreeLance(Empleado):

    def __init__(self,id,nombre,correo,tarifa_por_hora,horas_trabajadas):
        super().__init__(id,nombre,correo)
        self.__tarifa_por_hora = tarifa_por_hora
        self.__horas_trabajadas = horas_trabajadas

    @property
    def tarifa_por_hora(self):
        return self.__tarifa_por_hora
    
    @tarifa_por_hora.setter
    def tarifa_por_hora(self,nueva_tarifa):
        if nueva_tarifa > 0:
            self.__tarifa_por_hora = nueva_tarifa
        else:
            raise ValueError("La tarifa por hora debe ser mayor a cero")
    
    @property
    def horas_trabajadas(self):
        return self.__horas_trabajadas
    
    @horas_trabajadas.setter
    def horas_trabajadas(self,nuevas_horas):
        if nuevas_horas > 0:
            self.__horas_trabajadas = nuevas_horas
        else:
            raise ValueError("Las horas trabajadas deben ser mayores a cero")
    
    def calcular_salario(self):
        salario = self.__tarifa_por_hora * self.__horas_trabajadas
        self.registrar_pago(salario)
        return salario
    
    def __str__(self):
        return f"{super().__str__()} , Tarifa por hora: {self.__tarifa_por_hora}, Horas trabajadas: {self.__horas_trabajadas}"