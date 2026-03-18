from universidad import Universidad
from profesor import Profesor
from universitario import Universitario
from curso import Curso
import time

def main():
    universidad = Universidad("holaaaaa")

    while True:
        print("--- Menu ---")
        print("1.Aregar Estudiante")
        print("2.Agregar Profesor")
        print("3.Agregar Curso")
        print("4.Mostrar Estudiantes")
        print("5.Mostrar Cursos")
        print("6.Matricular estudiante en curso")
        print("7.Asignar profesor a curso")
        print("8.Ver cursos de un estudiante")
        print("9. Salir")

        try:
            while True:
                opcion = int(input("Ingrese una opcion (1-9): "))
                if opcion < 0 or opcion > 9:
                    print("Ingrese una opcion dentro del rango")
                else:
                    break
        except ValueError:
            print("Por favor, ingrese un numero valido")
        if opcion == 1:
            nombre = input("Nombre del estudiante: ")
            id_universidad = input("ID universitario: ")
            carrera = input("Carrera: ")
            estudiante = Universitario(nombre,id_universidad,carrera)
            universidad.agregar_estudiante(estudiante)
        
        elif opcion == 2:
            nombre = input("Nombre del profesor: ")
            id_universidad = input("ID universitario: ")
            especialidad = input("Especialidad: ")
            profesor = Profesor(nombre,id_universidad,especialidad)
            universidad.agregar_profesor(profesor)
        
        elif opcion == 3:
            nombre = input("Nombre del Curso: ")
            codigo = input("Codigo del Curso: ")
            while True:
                try: 
                    creditos = int(input("Cantidad de creditos: "))
                    if creditos < 0 or creditos > 4:
                        print("Cantidad de creditos invalida (1 -4 )")
                    else:
                        break
                except ValueError:
                    print("Ingrese un numero valido")
            while True: 
                try:
                    cupo_max = int(input(f"Cupo maximo de estudiantes de {nombre}: "))
                    if cupo_max < 0 :
                        print("El cupo debe ser mayor a 0")
                    else:
                        break
                except ValueError:
                    print("Ingrese un numero valido")
            curso = Curso (nombre,codigo,creditos,cupo_max)
            universidad.agregar_curso(curso)

        elif opcion == 4: 
            universidad.mostrar_estudiantes()
        
        elif opcion == 5:
            universidad.mostrar_cursos()
        
        elif opcion == 6: 
            universidad.mostrar_estudiantes()
            universidad.mostrar_cursos()
            id_estudiante = input("Ingrese el id del estudiante: ")
            codigo_curso = input("Ingrese el codigo del curso: ")

            estudiante = universidad.buscar_estudiante(id_estudiante)
            curso = universidad.buscar_curso(codigo_curso)

            if estudiante and curso:
                universidad.matricular_estudiante_a_curso(estudiante, curso)
        
        elif opcion == 7: 
            universidad.mostrar_profesores()
            universidad.mostrar_cursos()
            id_profesor = input("Ingrese el id del profesor: ")
            codigo_curso = input("Ingrese el codigo del curso: ")

            profesor = universidad.buscar_profesor(id_profesor)
            curso = universidad.buscar_curso(codigo_curso)
            
            if profesor and curso:
                universidad.asignar_profesor_a_curso(curso, profesor)
        
        elif opcion == 8: 
            universidad.mostrar_estudiantes()
            
            id_estudiante = input("Ingrese el ID del estudiante: ") 

            estudiante = universidad.buscar_estudiante(id_estudiante)

            if estudiante: 
                estudiante.mostrar_cursos_matriculados()
        elif opcion == 9:
            print("Saliendo del programa...")
            time.sleep(2)

if __name__ == "__main__":
    main()