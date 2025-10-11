# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher usando o laço for.

n = int(input('Qual o número para calculo da sua tabuada: '))

for c in range(1, 11):
    print(f'{n} X {c} = {c * n}')