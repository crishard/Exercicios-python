"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
contrataram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""
salario = float(input('Insira o valor do salário: '))

def aumento():

    if salario <= 280:
        percentual = '20%'
        percentualAumento = salario * (20/100)
        novoSalario = salario + (percentualAumento)
        print(f"""Salário antes do reajuste: R$ {salario}
        Percentual de aumento aplicado: {percentual}
        O valor do aumento: R$ {percentualAumento}
        Novo salário: R$ {novoSalario}""")

    if salario > 280 and salario < 700:
        percentual = '15%'
        percentualAumento = salario * (15/100)
        novoSalario = salario + (percentualAumento)
        print(f"""Salário antes do reajuste: R$ {salario}
        Percentual de aumento aplicado: {percentual}
        O valor do aumento: R$ {percentualAumento}
        Novo salário: R$ {novoSalario}""")

    if salario > 700 and salario < 1500:
        percentual = '10%'
        percentualAumento = salario * (10/100)
        novoSalario = salario + (percentualAumento)
        print(f"""Salário antes do reajuste: R$ {salario}
        Percentual de aumento aplicado: {percentual}
        O valor do aumento: R$ {percentualAumento}
        Novo salário: R$ {novoSalario}""")

    if salario <= 1500:
        percentual = '5%'
        percentualAumento = salario * (5/100)
        novoSalario = salario + (percentualAumento)
        print(f"""Salário antes do reajuste: R$ {salario}
        Percentual de aumento aplicado: {percentual}
        O valor do aumento: R$ {percentualAumento}
        Novo salário: R$ {novoSalario}""")

aumento()