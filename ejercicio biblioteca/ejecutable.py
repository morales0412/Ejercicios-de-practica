from biblioteca import Biblioteca
from libro import Libro
from socio_biblioteca import SocioBiblioteca

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n--- Menú Biblioteca ---")
        print("1. Agregar libro")
        print("2. Registrar socio")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Mostrar libros")
        print("6. Mostrar libros prestados de un socio")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            año = input("Año de publicación: ")
            libro = Libro(titulo, año, autor)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            nombre = input("Nombre del socio: ")
            id = input("ID del socio: ")
            socio = SocioBiblioteca(nombre, id)
            biblioteca.registrar_socio(socio)

        elif opcion == "3":
            id = input("ID del socio: ")
            socio = biblioteca.buscar_socio(id)
            if not socio:
                print(f"El socio con ID '{id}' no se encuentra en la biblioteca.")
                continue
            biblioteca.mostrar_libros()
            titulo = input("Título del libro: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                biblioteca.prestar_libro(socio, libro)

        elif opcion == "4":
            id = input("ID del socio: ")
            socio = biblioteca.buscar_socio(id)
            if not socio:
                print(f"El socio con ID '{id}' no se encuentra en la biblioteca.")
                continue
            titulo = input("Título del libro: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                biblioteca.devolver_libro(socio, libro)

        elif opcion == "5":
            biblioteca.mostrar_libros()

        elif opcion == "6":
            id = input("ID del socio: ")
            socio = biblioteca.buscar_socio(id)
            if socio:
                socio.mostrar_libros_prestados()

        elif opcion == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()