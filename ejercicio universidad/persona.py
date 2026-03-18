class Persona:
    
    def __init__ (self,nombre, id_universitario):
        self.nombre = nombre 
        self.id_universitario = id_universitario

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, ID Universitario: {self.id_universitario}"