# Crie uma tupla preenchida com os 20 primeiros colocados na tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a- Apenas os 5 primeiros colocados.
# b- Os últimos 4 colocados da tabela.
# c- Uma lista com os times em ordem alfabética.
# d- Em que posição na tabela está o time do Flamengo

# 18/10/2025
camp = 'Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Botafogo', 'Bahia', 'Fluminense', 'São Paulo', 'Vasco', 'Bragantino', 'Grêmio', 'Ceará', 'Corinthians', 'Atlético-MG', 'Internacional', 'Santos', 'Vitória', 'Fortaleza', 'Juventude', 'Sport'
print(f'Colocação dos times do Campeonato Brasileiro de Futebol em ordem: {camp}.')
print(f'Os 5 primeiros são: {camp[0:5]}.')
print(f'Os últimos 4 na tabela: {camp[-4:]}.')
print(f'A lista em ordem alfabética: {sorted(camp)}.')
print(f'O flamengo está na {camp.index('Flamengo')+1}º posição.')