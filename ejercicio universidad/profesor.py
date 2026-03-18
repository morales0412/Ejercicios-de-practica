from persona import Persona

class Profesor (Persona):
    
    def __init__ (self,nombre , id_universitario , especialidad):
        super().__init__(nombre,id_universitario)
        self.especialidad = especialidad
        self.cursos_dictados = []

    def asignar_curso(self,curso):
        if curso not in self.cursos_dictados:
            self.cursos_dictados.append(curso)
            print(f"Curso '{curso.nombre}' asignado a {self.nombre}.")
    
    def retirar_curso(self,curso):
        if not self.cursos_dictados:
            print(f"No hay cursos asignados a {self.nombre}")
            return
        elif curso in self.cursos_dictados:
            self.cursos_dictados.remove(curso)
            print(f"Curso '{curso.nombre}' retirado de {self.nombre}.")
            return
        else:
            print(f"El curso '{curso.nombre}' no esta asignado a {self.nombre}.")
            return
    
    def mostrar_cursos_dictados(self):
        if not self.cursos_dictados:
            print(f" No hay cursos dictados por {self.nombre}.")
            return
        print(f"Cursos dictados por {self.nombre}:")
        
        for curso in self.cursos_dictados:
            print(f" - {curso.nombre}")
        print(f"Total de cursos dictados: {len(self.cursos_dictados)}")