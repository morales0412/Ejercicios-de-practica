def crear_reporte(*args, **kwargs):
    """ "
    La función retorna un diccionario donde cada sección tiene su contenido, si una sección no tiene contenido en kwargs retorna "Sin contenido".
    """
    reporte = {}
    for arg in args:
        reporte[arg] = kwargs.get(arg, "Sin contenido")
    return reporte


print(
    crear_reporte(
        "introduccion",
        "desarrollo",
        "conclusion",
        introduccion="Este es el inicio",
        conclusion="Este es el final",
    )
)
