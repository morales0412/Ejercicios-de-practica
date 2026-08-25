personas = []

while True:
    print("--- Menu de opciones ---")
    print("1. Ingresar persona")
    print("2. Mostrar personas")
    print("3. Salir")

    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))

            if opcion < 1 or opcion > 3:
                print("Ingrese una opcion dentro del rango (1-3)")
                continue

            break

        except ValueError:
            print("Por favor, ingrese un numero valido.")

    if opcion == 1:
        # Verificar limite de personas
        if len(personas) >= 6:
            print("No se pueden ingresar mas personas, limite alcanzado.")
            continue

        # Datos personales
        while True:
            try:
                nombre = input("Ingrese el nombre de la persona: ")

                numero_identificacion = input(
                    "Ingrese el numero de identificacion de la persona: "
                )

                fecha_nacimiento = input(
                    "Ingrese la fecha de nacimiento de la persona (dd/mm/aaaa): "
                )

                correo_electronico = input(
                    "Ingrese el correo electronico de la persona: "
                )

                ciudad_residencia = input(
                    "Ingrese la ciudad de residencia de la persona: "
                )

                ciudad_origen = input("Ingrese la ciudad de origen de la persona: ")

                # Validar identificacion
                if len(numero_identificacion) != 10:
                    print("El numero de identificacion debe tener 10 digitos.")
                    continue

                # Validar correo
                if "@" not in correo_electronico or "." not in correo_electronico:
                    print("El correo electronico no es valido.")
                    continue

                break

            except ValueError:
                print("Por favor, ingrese datos validos.")

        # Canciones favoritas
        canciones = []

        for cancion in range(3):
            while True:
                try:
                    print(f"\nDatos de la cancion {cancion + 1}:")

                    nombre_cancion = input("Ingrese el nombre de la cancion: ")

                    artista = input("Ingrese el nombre del artista: ")

                    canciones.append(
                        {"nombre_cancion": nombre_cancion, "artista": artista}
                    )

                    break

                except ValueError:
                    print("Por favor, ingrese datos validos.")

        # Guardar persona
        personas.append(
            {
                "nombre": nombre,
                "numero identificacion": numero_identificacion,
                "fecha nacimiento": fecha_nacimiento,
                "correo electronico": correo_electronico,
                "ciudad residencia": ciudad_residencia,
                "ciudad origen": ciudad_origen,
                "canciones": canciones,
            }
        )

        print("Persona registrada correctamente.")
    elif opcion == 2:
        if not personas:
            print("No hay personas registradas.")
            continue
        while True:
            try:
                print("\n--- Personas registradas ---")
                for i, persona in enumerate(personas, start=1):
                    print(f"{i}. {persona['nombre']}")
                persona_seleccionada = int(input("Seleccion una persona por numero:"))
                if persona_seleccionada < 1 or persona_seleccionada > len(personas):
                    print("Ingrese un numero valido.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un numero valido.")
        persona = personas[persona_seleccionada - 1]
        print(f"\n--- Datos de {persona['nombre']} ---")
        print(f"Numero de identificacion: {persona['numero identificacion']}")
        print(f"Fecha de nacimiento: {persona['fecha nacimiento']}")
        print(f"Correo electronico: {persona['correo electronico']}")
        print(f"Ciudad de residencia: {persona['ciudad residencia']}")
        print(f"Ciudad de origen: {persona['ciudad origen']}")
        print("\n--- Canciones favoritas ---")
        for cancion in persona["canciones"]:
            print(f"Nombre de la cancion: {cancion['nombre_cancion']}")
            print(f"Artista: {cancion['artista']}")
            print("-----------------------------")
    elif opcion == 3:
        print("Saliendo del programa...")
        break
