# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import sample
from time import sleep
quant = int(input('Quantos jogos deseja sorteie: '))
lista = []

for n in range(quant):
    jogo = sorted(sample(range(1, 61), 6))
    lista.append(jogo)

for num in range(quant):
    print(f'Jogo {num+1}: {lista[num]}')
    sleep(0.5)

print('Boa sorte!!!')