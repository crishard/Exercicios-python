# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

qTurmas = int(input('Insira a quantidade de turmas: '))

i = 1
totalAlunos = 0
while i <= qTurmas:
    qAlunos = int(input(f'Insira a quantidade de alunos da turma {i}: '))
    i += 1
    if qAlunos > 40:
        print('A quantidade de alunos não pode ser maior que 40, coloque um valor menor ou igual a 40 para continuar')
    else:
        totalAlunos = totalAlunos + qAlunos
    
media = totalAlunos / qTurmas

print(f'A quantidade média de alunos é {media}')

