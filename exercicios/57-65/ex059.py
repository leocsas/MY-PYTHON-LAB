# Crie um programa que leia dois valores a mostra um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
r = 0

while r != 5:
    r = int(input('''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''))
    if r == 1:
        soma = v1 + v2
        print(f'A soma de {v1} e {v2} é {soma}.')
    elif r == 2:
        mult = v1 * v2
        print(f'A multiplicação de {v1} e {v2} é {mult}.')
    elif r == 3:
        if v1 > v2:
            print(f'O número maior é {v1}.')
        elif v2 > v1:
            print(f'O número maior é {v2}.')
    elif r == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))

# No vídeo de resolução tem a resposta em else pra caso o usuário erre e coloque um valor inválido.