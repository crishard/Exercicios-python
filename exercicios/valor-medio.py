# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qCds = int(input('Insira a quantidade de CDS comprados: '))

i = 1

valorTtotal = 0

while i <= qCds:
    valor = float(input(f'Insira o valor pago no CD n°{i}: '))
    i += 1
    if valor >= 0:
        valorTtotal = valorTtotal + valor
    else:
        print('O valor pago por CD não pode ser negativo!')

valorMedio = valorTtotal / qCds

print(f'''O valor total investido é de {valorTtotal}
O valor médio pago por CD é de {valorMedio}''')