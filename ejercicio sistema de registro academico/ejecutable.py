from universidad import Universidad
from estudiante import Estudiante
from estudianteBecado import EstudianteBecado
def main():
    universidad = Universidad()
    while True:
        print("\nMenu")
        print("1. Agregar estudiante")
        print("2. Buscar estudiante")
        print("3. Agregar materia a estudiante")
        print("4. Mostrar estudiantes por materia")
        print("5. Salir")

        while True:
            try:
                opcion = int(input("Seleccione una opcion:"))
                if opcion < 1 or opcion > 5:
                    print("Opcion no valida")
                    continue
                break
            except ValueError:
                print("Ingrese un valor valido")
        if opcion == 1:
            nombre = input("Ingrese el nombre del estudiante:")
            id_estudiante = input("Ingrese el ID del estudiante: ")
            becado = input("Es becado? (s/n): ").lower().strip()
            if becado == "s":
                porcentaje_beca = float(input("Ingrese el porcentaje de beca: "))
                estudiante = EstudianteBecado(nombre,id_estudiante,porcentaje_beca)
            else:
                estudiante = Estudiante(nombre,id_estudiante)
            universidad.agregar_estudiante(estudiante)
            print("Estudiante agregado exitosamente")
        elif opcion == 2:
            id_estudiante = input("Ingrese el ID del estudiante a buscar: ")
            estudiante = universidad.buscar_estudiante(id_estudiante)
            if estudiante:
                print(estudiante)
            else:
                print("El estudiante no esta registrado")
        elif opcion == 3:
            id_estudiante = input("Ingrese el ID del estudiante:  ")
            materia = input("Ingrese el nombre de la materia: ")
            estudiante = universidad.buscar_estudiante(id_estudiante)
            if estudiante:
                estudiante.agregar_materia(materia)
            else:
                print("El estudiante no esta registrado")
        elif opcion == 4:
            materia = input("Ingrese el nombre de la materia: ")
            estudiantes_materia = universidad.obtener_estudiantes_por_materia(materia)
            if estudiantes_materia:
                print("Estudiantes inscritos en la materia: ")
                for estudiante in estudiantes_materia:
                    print(estudiante)
            else: 
                print("No hay estudiantes inscritos en la materia")
        elif opcion == 5:
            print("Saliendo... ")
            break

if __name__ == "__main__":
    main()