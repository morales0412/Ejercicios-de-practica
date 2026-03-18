correos = ["juan@gmail.com", "pedro.com", "ana@outlook.com", "error_123", "sofia@web.es"]
validos = [correo for correo in correos if "@" in correo]
print(validos)