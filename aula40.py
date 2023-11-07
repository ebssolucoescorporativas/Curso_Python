""" Calculadora com while """
while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    oper = input('Digite o operador + - * /: ')
    try:
        int_num1 = int(num1)
        int_num2 = int(num2)
        if oper == '+':
            print(int_num1 + int_num2)
        elif oper == '-':
            print(int_num1 - int_num2)
        elif oper == '*':
            print(int_num1 * int_num2)
        elif oper == '/':
            print(int_num1 / int_num2)
        else:
            print('Operador inválido')


    except:
        print('Não foi informado um número inteiro')
    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break