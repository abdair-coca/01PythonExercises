# Cuenta cuántas vocales hay en una lista de caracteres.
# Ejemplo: ['a', 'b', 'e', 'i', 'o', 'x'] → 4

lista = ['a', 'b', 'e', 'i', 'o', 'x'] 

vocales = {'a', 'e', 'i', 'o', 'u'}

result =0
for i in lista:
    if i in vocales: 
        result += 1

print(result)
