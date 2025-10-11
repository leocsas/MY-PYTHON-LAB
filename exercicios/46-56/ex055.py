# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.
pesoM = 0
pesom = 0

for c in range(1, 6):
    peso = float(input(f'Insira o peso da {c}º pesspa: '))
    if c == 1:
        pesoM = peso
        pesom = peso
    elif pesoM < peso:
        pesoM = peso
    elif pesom > peso:
        pesom = peso

print(f'O maior peso é: {pesoM}KG')
print(f'O menor peso é: {pesom}KG')