asistencia_lunes = []
asistencia_viernes = []

def agregar_asistencia(dia, nombre):
    if dia == "lunes":
        asistencia_lunes.append(nombre)
    else:
        asistencia_viernes.append(nombre)

def alumnos_totales(lunes,viernes):
    return set(lunes).union(set(viernes))


def asistencia_perfecta(lunes,viernes):
    return set(lunes).intersection(set(viernes))

def solo_lunes(lunes,viernes):
    return set(lunes).difference(set(viernes))

def solo_viernes(lunes,viernes):
    return set(viernes).difference(set(lunes))

def asistieron_solo_una_vez(lunes,viernes):
    return set(lunes).symmetric_difference(set(viernes))

def mostrar_alumnos(alumnos):
    for alumno in alumnos:
        print(alumno)
def main():
    while True:
        print("\nMenu")
        print("1. Agregar asistencia")
        print("2. Alumnos totales")
        print("3. Asistencia perfecta")
        print("4. Solo lunes")
        print("5. Solo viernes")
        print("6. Asistieron solo una vez")
        print("7. Salir")

        while True:
            opcion = int(input("Ingrese una opcion: "))
            if opcion not in [1,2,3,4,5,6,7]:
                print("Ingrese un valor valido")
                continue
            break
        if opcion == 1:
            while True:
                dia = input("Ingrese el dia (lunes/viernes): ").lower().strip()
                if dia not in ["lunes", "viernes"]:
                    print("Ingrese un valor valido")
                    continue
                break
            nombre = input("Ingrese el nombre del alumno: ").strip()
            agregar_asistencia(dia,nombre)
            print("Asistencia agregada")
        elif opcion == 2:
            alumnos = alumnos_totales(asistencia_lunes, asistencia_viernes)
            print("Alumnos totales: ")
            mostrar_alumnos(alumnos)
        elif opcion == 3:
            alumnos = asistencia_perfecta(asistencia_lunes, asistencia_viernes)
            print("Alumnos que asistieron a los dos dias:")
            mostrar_alumnos(alumnos)
        elif opcion == 4:
            alumnos = solo_lunes(asistencia_lunes, asistencia_viernes)
            print("Alumnos que asistieron solo en lunes: ")
            mostrar_alumnos(alumnos)
        elif opcion == 5:
            alumnos = solo_viernes(asistencia_lunes, asistencia_viernes)
            mostrar_alumnos(alumnos)
        elif opcion == 6:
            alumnos = asistieron_solo_una_vez(asistencia_lunes,asistencia_viernes)
            mostrar_alumnos(alumnos)
        elif opcion == 7:
            print("Saliendo del programa...")
            break
        else:
            print("opcion no valida")

if __name__ == "__main__":
    main()