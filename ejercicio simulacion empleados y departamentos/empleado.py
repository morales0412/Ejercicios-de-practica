class Empleado: 
    def __init__ (self,nombre,departamento,salario):
        self.__nombre = nombre
        self.__departamento = departamento
        self.__salario = salario
    
    @property
    def salario(self):
        return self.__salario
    
    def calcular_bonificacion(self):
        return self.__salario * 0.1
    
    def obtener_salario_anual(self):
        return self.__salario * 12
    
    def __str__(self):
        return f"Empleado: {self.__nombre}, Departamento: {self.__departamento}, Salario: ${self.__salario}"
    
