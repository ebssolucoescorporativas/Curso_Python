"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
#print(nome)
#print(tamanho_nome)
#print(nome[3])
i = 0

nova_string = ''
while i < tamanho_nome:
    nova_string += '*' + nome[i] 
    i += 1
    
nova_string += '*'
print(nova_string)