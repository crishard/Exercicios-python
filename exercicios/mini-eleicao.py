# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
totalEleitores = int(input("Insira o número total de eleitores: "))
candidatoA = 0
candidatoB = 0
candidatoC = 0

while totalEleitores > 0:
    votosPossiveis = ['a', 'b', 'c', 'A', 'B', 'C']
    voto = input('Escolha em que candidato quer votar digitando a letra de cada um: "a", "b" ou "c": ')
    totalEleitores -= 1
    if voto in votosPossiveis:
        if voto == 'a' or voto == 'A':
            candidatoA = candidatoA + 1
        elif voto == 'b' or voto == 'B':
            candidatoB += 1
        elif voto == 'c' or voto == 'C':
            candidatoC += 1

    else:
        print('Por favar, rode novamente o programa e digite uma opção válida de votos')
        break
    
    if totalEleitores <= 0:
        print(f'''O total de votos do candidato A foi de {candidatoA}
O total de votos do candidato B foi de {candidatoB}
O total de votos do candidato C foi de {candidatoC}''')

