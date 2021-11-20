"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
"""
#coletando valores
num1 = float(input('Insira um valor qualquer: '))
num2 = float(input('Insira um outro valor qualquer: '))

#criando uma lista de possíveis operações e coletando a operação
operacoes = ['+', '-', '*', '/']
operacao = input('Qual operação deseja realizar: + [adição], - [subtração], * [multiplicação] ou / [divisão]')

#função para realizar a operação e verificar os resultados
def result(num1, num2):
    #verificando se a operação selecionada é válida
    if operacao in operacoes:

        #realizando a operação escolhida pelo usuário
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

    #caso a operação escolhida não seja válida
    else:
        print('Por favor, escolha uma operação válida')

    #verificando se o resultado é positivo ou negativo
    if res < 0:
        pn = 'Negativo'
    else:
        pn = 'Positivo'

    #verificando se o valor é par ou impar
    if res % 2 == 0:
        pi = 'par'
    else:
        pi = 'ímpar'
        
    #verificando se o valor é um inteiro ou um decimal 
    if res // 1 == res:
        di = 'interio'
    else:
        di = 'decimal'

    #imprimindo o resultado pedido
    print(f'O seu resultado é {res}, seu numero é {pn}, {pi} e {di}')

#chamando a função
result(num1, num2)