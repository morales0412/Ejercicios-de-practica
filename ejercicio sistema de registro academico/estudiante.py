class Estudiante:

    def __init__(self,nombre,id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.materias = set()
    
    def agregar_materia(self,materia):
        if materia in self.materias:
            print(f"El estudiante ya esta inscrito en la materia: {materia}")
            return
        self.materias.add(materia)
        print(f"Se ha inscrito al estudiante {self.nombre} en la materia: {materia}")
    
    def __str__ (self):
        return f"""{self.nombre} - {self.id_estudiante} - Materias: {', '.join(self.materias) if self.materias else 'Ninguna'}"""

