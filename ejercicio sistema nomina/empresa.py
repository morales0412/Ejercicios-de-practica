
class Empresa:
    def __init__(self):
        self.empleados = []
    
    def agregar_empleado(self,empleado):
        if any(e.id == empleado.id for e in self.empleados):
            print("El empleado ya existe")
        else:
            self.empleados.append(empleado)
        
    def mostrar_nomina(self):
        if not self.empleados:
            print("No hay empleados")
        else:
            for empleado in self.empleados:
                print(f"{empleado.nombre} {empleado.id} : {empleado.calcular_salario()}")
    
    def suma_nomina(self):
        if not self.empleados:
            print("No hay empleados")
        else:
            total = sum(empleado.calcular_salario() for empleado in self.empleados)
            print(f"La nomina total es: {total}")
    
    def buscar_empleado(self,id):
        for empleado in self.empleados:
            if empleado.id == id:
                return "El empleado existe"
        return "El empleado no existe"
    
    def eliminar_empleado (self,id):
        if not self.empleados:
            print("No hay empleados")
        else:
            for empleado in self.empleados:
                if empleado.id == id:
                    self.empleados.remove(empleado)
                    print("El empleado ha sido eliminado")
                    return
            print("El empleado no existe")