# Crie um programa que simule o funcionamento de um caixa eletrônico. No ínicio, pergunte ao usuário qual será o valor a ser sacado (Número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Obs: Considere que o caixa possui cédulas de 50, 20, 10 e 1.

print("--- Leo's Bank ---")

valor = int(input('Qual valor a ser retirado: '))
v = valor
cinq = vint = dez = cinco = um = 0

while True:
    while v > 0:
        if v >= 50:
            cinq = v // 50
            v = v % 50
        if v >= 20:
            vint = v // 20
            v = v % 20
        if v >= 10:
            dez = v // 10
            v = v % 10
        if v >= 5:
            cinco = v // 5
            v = v % 5
        if v >= 1:
            um = v // 1
            v = v % 1
    break

if cinq > 0:
    print(f'Você tem {cinq} cédulas de 50 reais.')
if vint > 0:
    print(f'Você tem {vint} cédulas de 20 reais.')
if dez > 0:
    print(f'Você tem {dez} cédulas de 10 reais.')
if cinco > 0:
    print(f'Você tem {cinco} cédulas de 5 reais.')
if um > 0:
    print(f'Você tem {um} cédulas de 1 real.')
        

print(f'Total retirado: {valor}')