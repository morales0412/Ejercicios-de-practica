from estudiante import Estudiante

class EstudianteBecado(Estudiante):
    
    def __init__ (self,nombre, id_estudiante,porcentaje_beca):
        super().__init__(nombre,id_estudiante)
        self.porcentaje_beca = porcentaje_beca
    
    def __str__(self):
        return f"{super().__str__()} -Porcentaje de beca: {self.porcentaje_beca}%"