# Dada una lista de enteros y un número objetivo, retorna todas las sublistas que suman ese número.
# Ejemplo: lista = [1, 2, 3, 4], objetivo = 5 → [[2, 3], [1, 4]]

lista = [1,2,3,4]
objetivo = 5
vistos = []
result = []

for num in lista:
    necesario = objetivo - num
    if necesario in vistos:
        result.append([necesario, num]) 
    vistos.append(num)

print(result)