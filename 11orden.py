# Dada una lista de tuplas (nombre, edad), retorna una lista ordenada por edad.
# Ejemplo: [('Ana', 22), ('Luis', 19), ('Pedro', 25)] → [('Luis', 19), ('Ana', 22), ('Pedro', 25)]
datos = [('Ana', 22), ('Luis', 19), ('Pedro', 25)] 

newdatos = sorted(datos, key=lambda x: x[1])

print(newdatos)