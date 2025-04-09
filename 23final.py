# Dada una lista como ['x', 'x', 'o', 'x', 'x', 'o', 'x'], detecta si hay tres 'x' seguidos
# como en el tres en línea. Retorna True si lo hay, False si no.

lista1 = ['o', 'x', 'x', 'x', 'o', 'x']  # tres x en medio
lista2 = ['x', 'x', 'x']                # justo al principio
lista3 = ['o', 'o', 'x', 'x', 'x', 'o'] # entre otros elementos
lista4 = ['x', 'x', 'x', 'x', 'x']      # más de tres x seguidos
lista5 = ['x', 'x', 'o', 'x', 'x']      # nunca hay 3 seguidas
lista6 = ['o', 'o', 'x', 'o', 'x']      # solo 'x' sueltas
lista7 = ['o', 'x', 'x', 'o', 'x']      # nunca llegan a tres

contador = 0
result = False
for elemento in lista6:
    if elemento == 'o':
        contador =0
    else:
        contador +=1
    if contador == 3:
        result = True
        break

print (result)