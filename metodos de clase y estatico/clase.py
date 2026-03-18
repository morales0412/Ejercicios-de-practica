# Metodo de clase = esta asociado directamente a la clase y no hay necesidad de crear un objeto para poder acceder al metodo
# Este debe recibir como primer parametro cls
import datetime

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        
    @classmethod
    def desde_anio_nacimiento(cls, nombre, anio):
        """
        Este es un método de clase.
        Recibe la clase misma como primer argumento (cls) en lugar de la instancia (self).
        Se usa comúnmente como un 'constructor alternativo'.
        """
        anio_actual = datetime.date.today().year
        edad = anio_actual - anio
        return cls(nombre, edad)

persona1 = Persona("Ana", 25)
persona1.saludar()

persona2 = Persona.desde_anio_nacimiento("Carlos", 1990)
persona2.saludar()