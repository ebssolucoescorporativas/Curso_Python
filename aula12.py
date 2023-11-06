nome = 'Eduardo Bueno da Silva'
altura = 1.71
peso = 90
imc = peso / (altura * altura)

''' f-strings '''
linha_1 = f'{nome}, tem, {altura} de altura,'
linha_2 =  f'pesa, {peso} quilos e seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)