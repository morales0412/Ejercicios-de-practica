import random

from habilidad.habilidad import Habilidad
from items.item import Item
from items.tienda import Tienda
from motor_combate.engine import MotorCombate
from personajes.asesino import Asesino
from personajes.mago import Mago
from personajes.tanque import Tanque


def crear_habilidad(nombre, daño_base, tipo_daño, enfriamiento, costo_mana, nivel_requerido, escalado, frase):
    return Habilidad(
        nombre,
        daño_base,
        tipo_daño,
        enfriamiento,
        costo_mana,
        nivel_requerido,
        escalado,
        frase,
    )


def crear_item(nombre, tipo, precio, bonificaciones):
    return Item(nombre, tipo, precio, bonificaciones)


def crear_catalogo_items():
    return {
        "Tanque": [
            crear_item("Coraza de Titanes", "Defensivo", 320, {"vida": 180, "resistencia_fisica": 14}),
            crear_item("Escudo del Bastion", "Defensivo", 290, {"vida": 120, "resistencia_magica": 12}),
            crear_item("Anillo de Fortaleza", "Utilidad", 210, {"mana": 40, "vida": 70, "resistencia_fisica": 8}),
            crear_item("Peto del Coloso", "Defensivo", 410, {"vida": 240, "resistencia_fisica": 18, "resistencia_magica": 10}),
        ],
        "Mago": [
            crear_item("Baston Arcano", "Ofensivo", 340, {"daño_magico": 28, "mana": 90}),
            crear_item("Amuleto de Llamas", "Ofensivo", 300, {"daño_magico": 22, "mana": 60}),
            crear_item("Manto de Cristal", "Utilidad", 260, {"vida": 50, "mana": 120, "resistencia_magica": 10}),
            crear_item("Corona Astral", "Ofensivo", 420, {"daño_magico": 36, "mana": 110, "resistencia_magica": 8}),
        ],
        "Asesino": [
            crear_item("Daga del Acechador", "Ofensivo", 330, {"daño_fisico": 34, "daño_magico": 8, "vida": 30}),
            crear_item("Filo de Sangre", "Ofensivo", 280, {"daño_fisico": 24, "resistencia_fisica": 5, "vida": 20}),
            crear_item("Botas Sombras", "Utilidad", 240, {"vida": 45, "mana": 20, "daño_fisico": 14}),
            crear_item("Garra del Sombra", "Ofensivo", 410, {"daño_fisico": 42, "resistencia_fisica": 6, "vida": 40}),
        ],
        "Comunes": [
            crear_item("Amuleto Vital", "Utilidad", 180, {"vida": 80, "mana": 50}),
            crear_item("Botas de Guerra", "Utilidad", 200, {"vida": 30, "daño_fisico": 10, "daño_magico": 10}),
        ],
    }


def crear_catalogo_personajes():
    return [
        crear_tanque("Aegor"),
        crear_tanque("Brakka"),
        crear_tanque("Torm"),
        crear_mago("Selene"),
        crear_mago("Iria"),
        crear_mago("Nox"),
        crear_asesino("Kael"),
        crear_asesino("Riven"),
        crear_asesino("Darius"),
    ]


def crear_tanque(nombre):
    stats = {
        "vida": 980,
        "mana": 180,
        "daño_fisico": 72,
        "daño_magico": 42,
        "resistencia_fisica": 28,
        "resistencia_magica": 22,
    }
    personaje = Tanque(nombre, stats)
    personaje.habilidades = [
        crear_habilidad(
            "Golpe de Escudo",
            85,
            "fisico",
            1,
            20,
            1,
            {"daño_fisico": 35, "vida": 5},
            f"{nombre} aplasta con su escudo.",
        ),
        crear_habilidad(
            "Muralla de Hierro",
            55,
            "fisico",
            2,
            25,
            3,
            {"vida": 8, "resistencia_fisica": 10},
            f"{nombre} se cubre con una muralla imposible de romper.",
        ),
        crear_habilidad(
            "Terremoto Protector",
            120,
            "fisico",
            3,
            40,
            6,
            {"vida": 10, "daño_fisico": 20},
            f"{nombre} hace temblar el campo de batalla.",
        ),
    ]
    return personaje


def crear_mago(nombre):
    stats = {
        "vida": 680,
        "mana": 360,
        "daño_fisico": 38,
        "daño_magico": 118,
        "resistencia_fisica": 14,
        "resistencia_magica": 20,
    }
    personaje = Mago(nombre, stats)
    personaje.habilidades = [
        crear_habilidad(
            "Lanza Arcana",
            95,
            "magico",
            1,
            25,
            1,
            {"daño_magico": 42, "mana": 10},
            f"{nombre} libera una lanza de energia arcana.",
        ),
        crear_habilidad(
            "Nova Elemental",
            140,
            "magico",
            2,
            45,
            3,
            {"daño_magico": 55, "mana": 15},
            f"{nombre} desata una nova elemental.",
        ),
        crear_habilidad(
            "Tormenta Astral",
            175,
            "magico",
            3,
            60,
            6,
            {"daño_magico": 68, "mana": 20},
            f"{nombre} convoca una tormenta de astros.",
        ),
    ]
    return personaje


def crear_asesino(nombre):
    stats = {
        "vida": 760,
        "mana": 240,
        "daño_fisico": 126,
        "daño_magico": 28,
        "resistencia_fisica": 18,
        "resistencia_magica": 14,
    }
    personaje = Asesino(nombre, stats)
    personaje.habilidades = [
        crear_habilidad(
            "Golpe Sombrio",
            105,
            "fisico",
            1,
            20,
            1,
            {"daño_fisico": 40, "daño_magico": 4},
            f"{nombre} emerge desde las sombras.",
        ),
        crear_habilidad(
            "Perforar Armadura",
            145,
            "fisico",
            2,
            35,
            3,
            {"daño_fisico": 55, "resistencia_fisica": 6},
            f"{nombre} rompe la defensa rival.",
        ),
        crear_habilidad(
            "Asesinato Perfecto",
            185,
            "fisico",
            3,
            50,
            6,
            {"daño_fisico": 80, "vida": 10},
            f"{nombre} ejecuta un remate perfecto.",
        ),
    ]
    return personaje


def mostrar_personajes(personajes):
    print("\n=== PERSONAJES DISPONIBLES ===")
    for indice, personaje in enumerate(personajes, start=1):
        print(
            f"{indice}. {personaje.nombre} - {personaje.tipo} | Vida {personaje.stats['vida']} | Mana {personaje.stats['mana']} | Dano fisico {personaje.stats['daño_fisico']} | Dano magico {personaje.stats['daño_magico']}"
        )


def mostrar_items(items_por_tipo):
    print("\n=== ITEMS DISPONIBLES ===")
    for tipo, items in items_por_tipo.items():
        print(f"{tipo}:")
        for item in items:
            print(f"  - {item}")


def crear_tienda():
    return Tienda(crear_catalogo_items())


def crear_roster_con_jugador(jugador):
    roster = []
    for personaje in crear_catalogo_personajes():
        if personaje.nombre == jugador.nombre:
            roster.append(jugador)
        else:
            roster.append(personaje)
    return roster


def equipar_items_iniciales_enemigo(motor, personaje, tienda):
    items_disponibles = tienda.items_para_tipo(personaje.tipo)
    cantidad = min(2, len(items_disponibles))
    items_elegidos = random.sample(items_disponibles, cantidad)
    motor.equipar_items(personaje, items_elegidos)


def fase_tienda(personaje, tienda):
    while True:
        print(f"\nOro disponible: {personaje.oro}")
        tienda.mostrar(personaje.tipo)
        eleccion = elegir_opcion_entera("Elige un item para comprar (0 para salir): ", 0, len(tienda.items_para_tipo(personaje.tipo)))
        if eleccion == 0:
            break
        try:
            item = tienda.comprar(personaje, eleccion)
            print(f"Compraste y equipaste {item.nombre}.")
            print(f"Oro restante: {personaje.oro}")
        except Exception as error:
            print(str(error))


def preparar_jugador(personaje):
    personaje.restaurar_combate()


def preparar_enemigo(motor, enemigo, tienda):
    enemigo.restaurar_combate()
    equipar_items_iniciales_enemigo(motor, enemigo, tienda)


def elegir_opcion_entera(mensaje, minimo, maximo):
    while True:
        opcion = input(mensaje).strip()
        if not opcion.isdigit():
            print("Ingresa un numero valido.")
            continue
        valor = int(opcion)
        if valor < minimo or valor > maximo:
            print("La opcion esta fuera de rango.")
            continue
        return valor


def equipar_paquete_inicial(motor, personaje, items_por_tipo):
    pool = items_por_tipo.get(personaje.tipo, [])
    if not pool:
        return
    cantidad = min(2, len(pool))
    items_elegidos = random.sample(pool, cantidad)
    motor.equipar_items(personaje, items_elegidos)


def main():
    personajes = crear_catalogo_personajes()
    tienda = crear_tienda()

    print("=== MOTOR DE COMBATE MOBA POR TURNOS ===")
    mostrar_personajes(personajes)
    mostrar_items(tienda.catalogo)

    eleccion = elegir_opcion_entera("\nElige tu personaje (1-9): ", 1, len(personajes))
    personaje_jugador = personajes[eleccion - 1]
    personaje_jugador.oro = 300
    personaje_jugador.restaurar_combate()

    print(f"\nHas elegido a {personaje_jugador.nombre} ({personaje_jugador.tipo}).")
    print("Empezas con 300 de oro para la tienda.")

    while personaje_jugador.vida_actual > 0:
        roster = crear_roster_con_jugador(personaje_jugador)
        motor = MotorCombate(roster)
        personaje_enemigo = motor.elegir_enemigo(personaje_jugador)
        preparar_enemigo(motor, personaje_enemigo, tienda)

        print(f"\nEl enemigo sera {personaje_enemigo.nombre} ({personaje_enemigo.tipo}).")
        print("\n=== ESTADO INICIAL ===")
        print(personaje_jugador)
        print("Items:", ", ".join(item.nombre for item in personaje_jugador.items) or "Sin items")
        print(personaje_enemigo)
        print("Items enemigo:", ", ".join(item.nombre for item in personaje_enemigo.items) or "Sin items")

        ganador = motor.batalla(personaje_jugador, personaje_enemigo)

        if ganador is not personaje_jugador:
            print(f"\n{personaje_jugador.nombre} fue derrotado. Fin de la partida.")
            break

        print(f"\n{ganador.nombre} queda victorioso.")
        fase_tienda(personaje_jugador, tienda)
        preparar_jugador(personaje_jugador)

        continuar = input("\nPresiona ENTER para buscar otro enemigo o escribe 'salir' para terminar: ").strip().lower()
        if continuar == "salir":
            break

    print("\nPartida finalizada.")


if __name__ == "__main__":
    main()