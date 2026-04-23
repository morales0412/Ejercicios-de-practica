class UserValidator:
    caracteres_especiales = {"@", "#", "$", "%", "&", "*"}

    @staticmethod
    def validate_password(password):
        if len(password) < 10:
            print("La contraseña debe ser mayor a 10 caracteres")
            return False
        if not any(valor.isdigit() for valor in password):
            print("La contraseña debe tener al menos un numero")
            return False
        if not any(valor in UserValidator.caracteres_especiales for valor in password):
            print("La contraseña debe tener al menos un caracter especial")
            return False
        return True
