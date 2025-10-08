# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá exibir na tela se o usuário venceu ou perdeu.
import random

n = random.randint(0, 5)

print('-=-' * 15)
m = int(input('Escolhi um número de 0 a 5, tente acertar: '))

if n == m:
    print('Parabéns, você acertou!')

else:
    print(f'Infelizmente você errou. O número escolhido era: {n}.')

# Idéia da linha pega no vídeo de resolução