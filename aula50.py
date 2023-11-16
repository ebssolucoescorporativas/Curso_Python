"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Eduardo')
i = 0
indices = range(len(lista))
print(indices)
for indice in indices:
    print(indice,lista[indice], type(lista[indice]))