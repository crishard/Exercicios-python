from random import randint

numero = randint(100000000, 999999999) #gera os primeiros nove números do cpf

cpf = []
c = [numero]
cpf.append(numero)
#Cria o décimo número do CPF válido, seguindo as regras dos últimos dígitos do CPF
dv = sum(c)
digito1 = 11 - (dv % 11)
digito10 = 0
if digito1 > 9:
    digito10 == 0
else:
    digito10 == digito1
c.append(digito10)
cpf.append(digito10)

#Cria o décimo primeiro número do CPF válido, seguindo as regras dos últimos dígitos do CPF
df = sum(c)
digito2 = 11 - (df % 11)
digito11 = 0
if digito2 > 9:
    digito11 = 0
else:
    digito11 = digito2
#unindo todos os digitos em uma lista
cpf.append(digito11)
#imprimindo o CPF, somente os números 
print(*cpf, sep='')
