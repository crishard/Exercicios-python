# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que 
# leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior 
# temperaturas informadas, bem como a média das temperaturas.

temperaturas = []

r = 's'

while r == 's':
    temp = float(input('Insir o valor da temperatura em °C: '))
    temperaturas.append(temp)

    r = input('Deseja adicionar uma nova temperatura? (s) Sim ou (n) Não: ')

    if r == 'n':
        menortemperatura = min(temperaturas)
        maiortemperatura = max(temperaturas)
        mediatemperaturas = sum(temperaturas) / len(temperaturas)

        print(f'''A maior temperatura é: {maiortemperatura}
A menor temperatura é {menortemperatura}
A média das temperaturas é {mediatemperaturas}''')