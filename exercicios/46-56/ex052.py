# Faça um programa que leia um número interio e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
cont = 0

for c in range(1, n+1):
    if n % c == 0:
        cont += 1
if cont == 2:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo.')

# No vídeo de resolução ele utilizou as cores.