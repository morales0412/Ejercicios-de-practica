empresa = {
    "nombre": "TechCorp",
    "departamentos":{
        "IT": {
            "empleados" : 10,
            "presupuesto": 50000

        },
        "Ventas":{
            "empleados": 5,
            "presupuesto": 30000
        }
    }
}
print(empresa["departamentos"]["Ventas"]["presupuesto"])