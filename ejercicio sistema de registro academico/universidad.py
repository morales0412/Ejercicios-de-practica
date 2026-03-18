class Universidad:
    def __init__ (self):
        self.__estudiantes = {}
    
    def agregar_estudiante(self,estudiante):
        if estudiante.id_estudiante in self.__estudiantes:
            print(f"El estudiante {estudiante.id_estudiante} ya esta registrado")
            return
        self.__estudiantes[estudiante.id_estudiante] = estudiante
        print(f"Se ha registrado al estudiante {estudiante.id_estudiante}")
    
    def buscar_estudiante (self,id_estudiante):
        if id_estudiante in self.__estudiantes:
            return self.__estudiantes[id_estudiante]
        return None
    
    def obtener_estudiantes_por_materia(self,materia):
        estudiantes_materia = []
        for estudiante in self.__estudiantes.values():
            if materia in estudiante.materias:
                estudiantes_materia.append(estudiante)
        return estudiantes_materia
    