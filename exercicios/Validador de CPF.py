#a válidação do CPF depende dos dois últimos dígitos do número, onde existe uma regra específica para validação
x = 1
cpf = []
c = []
for i in range(11):
    n = int(input(f'Insira o {x}° do seu CPF: '))
    cpf.append(n)
    i += 1
    x += 1
c = cpf[0:9]
r = []
v = 10
for i in c:
    x = i * v
    v = v -1
    r.append(x)
    i += 1
#valindando o décimo número do CPF
dv = sum(r)
digito1 = 11 - (dv % 11)
digito10 = 0
if digito1 > 9:
    digito10 == 0
else:
    digito10 == digito1

c.append(digito10)
q = []
g = 11
for i in c:
    m = i * g
    g = g - 1
    q.append(m)
    i += 1
#validando o décimo primeiro número do CPF
df = sum(q)
digito2 = 11 - (df % 11)
digito11 = 0
if digito2 > 9:
    digito11 = 0
else:
    digito11 = digito2

c.append(digito11)

if c == cpf:
    print('CPF válido')
else:
    print('CPF inválido!')