"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
"""
num1 = float(input('Insira um valor qualquer: '))
num2 = float(input('Insira um outro valor qualquer: '))

operacoes = ['+', '-', '*', '/']
operacao = input('Qual operação deseja realizar: + [adição], - [subtração], * [multiplicação] ou / [divisão]')
def result(num1, num2):
    if operacao in operacoes:
        if operacao == '+':
            res = num1 + num2

        if operacao == '-':
            res = num1 + num2

        if operacao == '*':
            res = num1 * num2

        if operacao == '/':
            if num2 < num1:
                print('Para realizar uma divisão, seu denominador não pode ser maior que o numerador')
            else:
                res = num1 / num2
    else:
        print('Por favor, escolha uma operação válida')

    if res < 0:
        pn = 'Negativo'
    else:
        pn = 'Positivo'

    if res % 2 == 0:
        pi = 'par'
    else:
        pi = 'ímpar'

    if res // 1 == res:
        di = 'interio'
    else:
        di = 'decimal'

    print(f'O seu resultado é {res}, seu numero é {pn}, {pi} e {di}')

result(num1, num2)