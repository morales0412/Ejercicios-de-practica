class Persona: 
    def __init__ (self,nombre,id):
        self.nombre = nombre
        self.id = id
    
    def __str__ (self):
        return f"Persona(nombre = {self.nombre}, id = {self.id})"