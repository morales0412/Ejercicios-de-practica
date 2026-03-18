class Empresa:
    def __init__(self):
        self.__empleados = {}

    def agregar_empleado(self, *empleado):
        for emp in empleado:
            self.__empleados[emp.id] = emp
            print(f"Se ha agregado exitosamente al empleado con el ID: {emp.id}")    

    def buscar_empleado(self, id):
        empleado = self.__empleados.get(id)
        if not empleado:
            print(f"El empleado con el ID: {id} no se encuentra en la empresa")
        return empleado
    
    def obtener_nomina_total(self):
        if not self.__empleados:
            print("No hay empleados en la empresa")
            return 0
        nomina_total = sum(emp.calcular_salario() for emp in self.__empleados.values())
        return nomina_total
    
    def filtrar_por_tipo(self, tipo_empleado):
        empleados_filtrados = {emp_id: emp for emp_id, emp in self.__empleados.items() if isinstance(emp, tipo_empleado)}
        return empleados_filtrados
    
    def ejecutar_pago(self):
        for emp in self.__empleados.values():
            salario = emp.calcular_salario()
            print(f"Se ha realizado el pago del empleado con el ID: {emp.id} por un monto de {salario:.2f}")
    