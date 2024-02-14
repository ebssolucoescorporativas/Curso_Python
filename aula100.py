# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
from aula100_package import aumenta_10_por_cento, produtos
print("Produtos originais")
print(*produtos, sep='\n')
novos_produtos = copy.deepcopy(produtos)
novos_produtos = aumenta_10_por_cento(novos_produtos)
print("Produtos com aumento")
print(*novos_produtos, sep='\n')

# print(novos_produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
print("Produtos decrescente")
novos_produtos = sorted(novos_produtos, key=lambda item: item['nome'], reverse=True)
print(*novos_produtos, sep='\n')
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
print("Produtos crescente")
novos_produtos_nome = copy.deepcopy(novos_produtos)
novos_produtos_nome = sorted(novos_produtos_nome, key=lambda item: item['nome'])
print(*novos_produtos_nome, sep='\n')
# Ordene os produtos por preco crescente (do menor para maior)
novos_produtos_valor_maior = sorted(novos_produtos_nome, key=lambda item: item['preco'], reverse=True)
print("Maiores preços")
print(*novos_produtos_valor_maior, sep='\n')
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
print("Menor preço")
novos_produtos_valor_menor = copy.deepcopy(novos_produtos_valor_maior)
novos_produtos_valor_menor = sorted(novos_produtos_valor_menor, key=lambda item: item['preco'])
print(*novos_produtos_valor_menor, sep='\n')