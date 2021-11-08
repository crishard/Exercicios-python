"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por
 uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação 
 e o número de dias em atraso e passar estes valores para a função valorPagamento, que 
 calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa 
 deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a 
 pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero 
 para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, 
 que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser 
 ago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando 
 houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso. 

"""
vp = 1
total= []
a = 0
while vp != 0:
    a += 1
    vp = float(input('Insira o valor da sua prestação: '))
    if vp == 0:
        break
    nd = int(input('Insira o número de dias em atraso: '))

    def valorPagamento(vp, nd):
        if nd > 0:
            return vp + (vp * 3/100) + ((vp * 0.1/100) * nd)
        return 'Não houve atraso no seu pagamento'

    resultado = valorPagamento(vp, nd)
    total.append(resultado)
    print(resultado)
print('''====================================== \n''' * 2)
print('     FECHAMENTO DIÁRIO DO CAIXA      ')
print(f'O numero total de prestações pagas no dia foi de {a-1}, dando um total de R$: {sum(total)}')
print('''====================================== \n''' * 2)

