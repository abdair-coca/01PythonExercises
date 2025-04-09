# Dadas dos listas, retorna los elementos comunes sin duplicados.
# Ejemplo: [1,2,3,4], [3,4,5,6] → [3, 4]

import re

lista1, lista2 = [1,2,3,4], [3,4,5,6]
lista1, lista2 = set(lista1), set(lista2)
result =[]

for elemento in lista1:
    if elemento in lista2:
        result.append(elemento)

print(result)