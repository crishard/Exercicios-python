"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

cidadeA = 80000
cidadeB = 200000

taxaA = (3/100)
taxaB = (1.5/100)
i = 0


while cidadeA < cidadeB:
    cidadeA = cidadeA + (cidadeA * (taxaA))
    cidadeB = cidadeB + (cidadeB * (taxaB))
    i += 1

print(f"É necessário {i} anos para que a cidade A iguale ou ultrapasse a cidade B em população")
