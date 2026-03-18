
class ConversorTemperatura:
    """
    Ejemplo de una clase con métodos estáticos.
    Los métodos estáticos no requieren acceso a atributos de la instancia (self)
    ni atributos de la clase (cls). Son como funciones normales pero agrupadas en una clase
    por organización.
    """
    
    @staticmethod
    def celsius_a_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_a_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# NO es necesario crear un objeto (instancia) para usarlo
# Se llama directamente desde el nombre de la clase
temp_f = ConversorTemperatura.celsius_a_fahrenheit(25)
print(f"25°C son {temp_f}°F")

temp_c = ConversorTemperatura.fahrenheit_a_celsius(77)
print(f"77°F son {temp_c}°C")

