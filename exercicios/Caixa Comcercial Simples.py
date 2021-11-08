"""
Caixa comercial simples
informar o tipo do produto
informar a quantidade de produtos e o valor de cada produto 
calcula o valor total
formas de pagamento 
descontos de 10% em pagamentos a vista em espécie ou no cartão
e acréscimos de 5% no valor total sendo parcelado em mais de 6x
sendo permmitido o parcelamento somente se o valor da parcela for maio ou igual a 35 reais mensais 
imprimir um comprovante informando cada informação
"""

produtos = []
quantidade = []
valores = []

print('==== Bem vindo, este é nosso sistema virtual de pagamento! ====')
r = 's'
x = 1
while r == 's':
    produto = input(f'Insira o {x}° produto da compra: ')
    x += 1
    produtos.append(produto)
    qtd = float(input('Insira a quantidade (seja em kg ou unidades) desse mesmo produto que foi comprado: ')) #float pro caso de compra de carne
    quantidade.append(qtd)
    valor = float(input('Insira o valor unitário deste mesmo produto: '))
    vf = qtd * valor
    valores.append(vf)
    r = input('existe mais algum produto nas compras desse cliente [s/n]?  ')

def caixa(): #Imprime quais são os produtos, a quantidaa, o valor e o toal da compra, com o aviso final
    print(f'''                   ======  Recibo  ======
    Produto            Quantidade          Valor a pagar'''
    )
    p = len(produtos)

    a = 1 #para pegar todos os produtos inseridos 
    i = 0 #vai servir como indíce para os produtos dentro do laço
    while a <= p:
        
        print(f'''{produtos[i]}                   {quantidade[i]}          {valores[i]}''')
        a += 1
        i += 1
    if a > p:
        print(f'''Total da compra                        {sum(valores)}
        lembrando que os valores exibidos ao lado do produto são correspondentes ao que será
        pago por todas as unidas do mesmo.''')

if r != 's':
    caixa()

pagamento = input('Qual forma de pagamento deseja usar(cartao \ especie): ')

def pagar(): #verifica as formas de pagamento e imprime o valro exato a ser pago

    if pagamento == 'cartao':
        qtdParcelas = int(input('Em quantas parcelas deseja efetuar o seu pagametnto: '))
        if qtdParcelas == 1:
            totalPagar = sum(valores) - (sum(valores) * (10/1000))
            print(f'O total a ser pago pelo cliente é: R$ {totalPagar} ')
        else:
            parcela = sum(valores) / qtdParcelas
        if parcela < 35:
            print(f'Você não poderá parcelar esse seu produto em {qtdParcelas} pois a mensalidade fica abaixo do permitido!')
        else: 
            print(f'O valor mensal cobrado em seu cartão será de: R${parcela} durante {qtdParcelas} meses!')
        if qtdParcelas > 6:
            novaParcela = parcela + (parcela * (5/100))
            print(f'O valor a mensal cobradi em seu cartão será de: R$ {novaParcela} durante {qtdParcelas} meses!')
    if pagamento == 'especie':
        totalPagar = sum(valores) - (sum(valores) * (10/1000))
        print(f'O total a ser pago pelo cliente é: R$ {totalPagar} ')
    else:
        print('Error! Por favor, insira novamente os produtos e uma forma de pagamento válida')

if pagamento != 'shhshs':
    pagar()
print('====== Obrigado pela preferência, volte sempre! ======')
