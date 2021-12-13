'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''

#primera forma de fazer sem biblioteca, porém, não imprime a parte do cálculo ex "5 . 4 . 3 . 2 . 1"
num = int(input('Insira um número inteiro para calcular o seu fatorial: '))

i = 0

while num > 1:
    fat = num * (num -1)
    i += 1
print(f'!{num} = {fat}') 


#segunda forma, com biblioteca e capturando o cálculo
import math
num = int(input("Fatorial de: "))
aux = num
fatorial = math.factorial(num)

for i in range(num - 1):
    print(aux, end=" . ")
    aux -= 1
print(fatorial)