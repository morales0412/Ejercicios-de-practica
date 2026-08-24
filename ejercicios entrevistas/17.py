class Usuario:
    """Representa un usuario con validaciones en sus atributos."""

    def __init__(self, nombre, email, edad, password):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.password = password

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        if not all(c.isalpha() or c.isspace() for c in valor):
            raise ValueError("El nombre solo puede contener letras y espacios.")
        self._nombre = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        partes = valor.split("@")
        if len(partes) != 2 or "." not in partes[1]:
            raise ValueError("Email inválido, debe contener '@' y '.' después del '@'.")
        self._email = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int):
            raise ValueError("La edad debe ser un número entero.")
        if valor < 0 or valor > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        self._edad = valor

    @property
    def password(self):
        return "*" * len(self._password)

    @password.setter
    def password(self, valor):
        if len(valor) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
        if not any(c.isupper() for c in valor):
            raise ValueError("La contraseña debe contener al menos una mayúscula.")
        if not any(c.isdigit() for c in valor):
            raise ValueError("La contraseña debe contener al menos un número.")
        self._password = valor

    def __str__(self):
        return f"Usuario: {self.nombre} | Email: {self.email} | Edad: {self.edad}"


try:
    usuario = Usuario("Juan Perez", "juan@gmail.com", 25, "Password1")
    print(usuario)
    print(usuario.password)  # ********
    usuario.email = "correo_invalido"
except ValueError as e:
    print(e)
