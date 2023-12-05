# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

# Crie uma função fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar



def multiplica(*args):

    multiplo = 1

    for numero in args:
        multiplo *= numero
    return multiplo

def parimpar(a):
    if a % 2 == 0:
        return 'PAR'
    return 'ÍMPAR'

fator = multiplica(1,2,3,4,5,6)
print(fator)

resultado = parimpar(5)
print(resultado)