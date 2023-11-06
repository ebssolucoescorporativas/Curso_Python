"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
numero = input('Digite um número: ')
try:
    numero_int  = int(numero)
    if numero_int % 2 == 0:
        print(f'O numero {numero_int} é um numero par')
    else:
        print(f'O numero {numero_int} é um numero ímpar')
        
except:
    print('Não é um numero inteiro')
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""



hora = input('Digite uma hora: ')
try:
    hora_int = int(hora)
    if hora_int <= 11:
        print('Bom dia!')
    elif hora_int <= 17:
        print('Boa tarde!')
    elif hora_int <= 23:
        print('Boa noite!')
    else:
        print('Não é uma hora válida!')
except:
    print('Não é uma hora válida!')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""
nome = input('Digite seu nome: ')
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
"""