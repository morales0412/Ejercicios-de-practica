from perro import Perro
from gato import Gato
from refugio import Refugio
from time import sleep

refugio = Refugio()


def pedir_datos():

    while True:
        tipo_animal = input("Ingrese el tipo de animal(perro/gato): ").lower().strip()
        if tipo_animal not in ["perro","gato"]:
            print("Tipo de animal no valido")
            continue
        break
    nombre = input("Ingrese el nombre: ")
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad < 0:
                print("Edad no valida")
                continue
            break
        except ValueError:
            print("Edad no valida")
    if tipo_animal == "perro":
        raza = input("Ingrese la raza: ")
        animal = Perro(nombre,edad,raza)
    else:
        color_piel = input("Ingrese el color de piel: ")
        animal = Gato(nombre,edad,color_piel)
    return animal

def main():
    while True:
        print("1. Agregar animal")
        print("2. Mostrar animales")
        print("3. Hora de siesta")
        print("4. Salir")
        while True:
            try:
                opcion = int(input("Seleccione una opcion:"))
                if opcion not in [1,2,3,4]:
                    print("Opcion no valida")
                    continue
                break
            except ValueError:
                print("Opcion no valida")
        if opcion == 1:
            animal = pedir_datos()
            refugio.admitir_animal(animal)
        elif opcion == 2:
            refugio.listar_residentes()
        elif opcion == 3:
            refugio.hora_siesta()
        else:
            print("Saliendo del programa...")
            sleep(2)
            break
if __name__ == "__main__":
    main()