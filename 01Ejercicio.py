# Dada una lista de números, retorna la suma de todos los números pares.
# Ejemplo: [1, 2, 3, 4, 5, 6] → 12

lista = [1, 2, 3, 4, 5, 6]

lista = sum([x for x in lista if x%2==0])

print(lista)