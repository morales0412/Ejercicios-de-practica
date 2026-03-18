from manager.libreria_manager import LibreriaManager
from usuarios.standard_user import StandardUser
from usuarios.premium_user import PremiumUser
from usuarios.librarian import Librarian
from libros.book import Book
from excepciones.base import LibraryError


def main():
    manager = LibreriaManager()

    try:
        # ---- crear usuarios ----
        user1 = StandardUser("U1", "Andres")
        user2 = PremiumUser("U2", "Carlos")
        librarian = Librarian("L1", "Admin")

        manager.registrar_usuario(user1)
        manager.registrar_usuario(user2)
        manager.registrar_usuario(librarian)

        # ---- crear libros ----
        book1 = Book("B1", "1984", "George Orwell", "Novela", "disponible")
        book2 = Book("B2", "Dracula", "Bram Stoker", "Terror", "disponible")

        manager.registrar_libro(book1)
        manager.registrar_libro(book2)

        # ---- crear préstamo ----
        manager.crear_prestamo("P1", "U2", "B1")
        print("[OK] Préstamo creado correctamente (U2)")

        # ---- renovar préstamo ----
        manager.renovar_prestamo("P1")
        print("[OK] Préstamo renovado correctamente")

        # ---- cerrar préstamo ----
        manager.cerrar_prestamo("P1")
        print("[OK] Préstamo cerrado correctamente")

        # ---- Generar ERROR INTENCIONAL ----
        print("\n--- Intentando operación inválida ---")
        # Intentar renovar un préstamo ya cerrado (debería fallar)
        manager.renovar_prestamo("P1")

    except LibraryError as e:
        print(f"[ERROR] Error de operación: {e}")

    except Exception as e:
        print("[ERROR] Error inesperado")
        print(e)

    else:
        print("[OK] Todas las operaciones se ejecutaron correctamente")

    finally:
        print("[INFO] Sistema de biblioteca finalizado")


if __name__ == "__main__":
    main()
