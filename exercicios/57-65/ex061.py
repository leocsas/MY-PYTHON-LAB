# Refaça o DESAFIO 051, lendo o primeiro termo a a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
v = 10

while v > 0:
    print(t)
    t += r
    v -= 1

# No vídeo de resolução ele utilizou um contador que vai até o 10.