# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

from aula100_package import aumenta_10_por_cento

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = aumenta_10_por_cento(produtos.copy())

print(novos_produtos)

# Ordene os produtos por nome decrescente (do maior para menor)

novos_produtos = sorted(novos_produtos, key=lambda item: item['nome'], reverse=True)
print(novos_produtos)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
novos_produtos_nome = novos_produtos.copy()
novos_produtos_nome = sorted(novos_produtos_nome, key=lambda item: item['nome'])
print(novos_produtos_nome)
# Ordene os produtos por preco crescente (do menor para maior)
novos_produtos_valor_maior = sorted(novos_produtos_nome, key=lambda item: item['preco'], reverse=True)
print(novos_produtos_valor_maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
novos_produtos_valor_menor = novos_produtos_valor_maior.copy()
novos_produtos_valor_menor = sorted(novos_produtos_valor_menor, key=lambda item: item['preco'])
print(novos_produtos_valor_menor)