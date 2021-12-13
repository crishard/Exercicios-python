'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final 
da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, 
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
'''
#listas para armazenar os valores
alturas = []
pesos = []
codigos = []

#para iniciar o looping sem valor definido
cod = True

while cod > 0:
    cod = int(input('Insira o seu código: '))
    #ferifica se o código é igual a 0 e encerra o laço
    if cod == 0:
        break
    #continua pedindo os dados e adicionando eles as listas, caso o código não seja igual a 0
    else:
        p = float(input('Insira o seu peso: '))
        a = float(input('Insira a sua altura: '))
        alturas.append(a)
        pesos.append(p)
        codigos.append(cod)

#capturando  o mais alto e o mais baixo
maisAlto = max(alturas)
maisBaixo = min(alturas)

#capturando o mais magro e o mais gordo
maisMagro = min(pesos)
maisGordo = max(pesos)

#pegando o código do mais alto e do mais baixo 
codMaisAlto = codigos[alturas.index(max(alturas))] 
codMaisBaixo = codigos[alturas.index(min(alturas))]

#pegando o código do mais magro e do mais gordo 
codMaisGordo = codigos[pesos.index(max(pesos))]
codMaisMagro = codigos[pesos.index(min(pesos))]

#calculando as médias
mediaPesos = sum(pesos) / len(pesos)
mediaAlturas = sum(alturas) / len(alturas)

#imprimindo o resultado que foi pedido 
print(f'''O mais alto é o de código n°: {codMaisAlto} com {maisAlto}m
O mais baixo é o de código n°: {codMaisBaixo} com {maisBaixo}m
O mais Gordo é o de código n°: {codMaisGordo} com {maisGordo}kg
O mais Magro é o de código n°: {codMaisMagro} com {maisMagro}kg
A média de altuas é: {mediaAlturas}m
A média de pesos é; {mediaPesos}''')