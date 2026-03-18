permisos_requeridos = {"lectura", "escritura", "edicion", "eliminacion"}
permisos_usuario = {"lectura", "escritura", "analisis"}

verificacion = permisos_requeridos.issuperset(permisos_usuario)
print(verificacion)
permisos_usuario.add("eliminacion")
diferencia = permisos_requeridos.difference(permisos_usuario)
print(diferencia)