class Temperatura:
    """
    Clase para representar una temperatura y realizar conversiones entre Celsius y Fahrenheit.
    """

    unidad_por_defecto = "Celsius"

    def __init__(self, valor):
        self.valor = valor

    @classmethod
    def cambiar_unidad_por_defecto(cls, nueva_unidad):
        if not isinstance(nueva_unidad, str):
            raise ValueError("La nueva unidad debe ser una cadena de texto.")
        unidades_validas = ["Celsius", "Fahrenheit"]
        if nueva_unidad not in unidades_validas:
            raise ValueError(
                f"La nueva unidad debe ser una de las siguientes: {', '.join(unidades_validas)}"
            )
        cls.unidad_por_defecto = nueva_unidad

    @staticmethod
    def convertir_a_fahrenheit(celsius):
        if not isinstance(celsius, (int, float)):
            raise ValueError("La temperatura debe ser un numero.")
        return (celsius * 9 / 5) + 32

    @staticmethod
    def convertir_a_celsius(fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            raise ValueError("La temperatura debe ser un numero.")
        return (fahrenheit - 32) * 5 / 9


print(Temperatura.convertir_a_fahrenheit(25))
