# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

resultados = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)
}

for v in resultados:
    print(f'O {v} tirou: {resultados[v]}')
    sleep(1)

ordem = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('-=' * 13)

for i, v in enumerate(ordem):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)