# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpitas foram necessários para vencer.

import random

n = random.randint(0, 10)
r = 0
while n != r:
    r = int(input('Digite o número de 0 a 10 até acertar: '))
print('Parabéns, você acertou!')