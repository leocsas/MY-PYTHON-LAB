# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

m = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        m[linha].append(int(input(f'Insira valor para [{linha}, {coluna}]: ')))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{m[linha][coluna]:^5}]', end='')
    print()