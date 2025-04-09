# Verifica si una lista es un palíndromo.
# Ejemplo: [1, 2, 3, 2, 1] → True

lista = [1, 2, 3, 2, 1]

print(lista == list(reversed(lista)))
