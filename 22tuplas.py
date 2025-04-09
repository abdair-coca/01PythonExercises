# Dada una lista de tuplas (nombre, [notas]), retorna un diccionario con nombre y promedio de notas
# y luego filtra solo los que tienen promedio mayor a 60.
# Ejemplo: [('Ana', [80, 90]), ('Luis', [50, 40])] → {'Ana': 85.0}
estudiantes = [
    ('Ana', [80, 90, 85]),
    ('Luis', [50, 40, 55]),
    ('María', [70, 75, 80]),
    ('Juan', [60, 60, 60]),
    ('Pedro', [30, 50, 40]),
    ('Lucía', [100, 95, 90])
]

estudiantes =[[estudiante[0], sum(estudiante[1])/3]for estudiante in estudiantes]
print(sorted(estudiantes, key=lambda x: x[1], reverse=True))