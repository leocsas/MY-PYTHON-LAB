# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostrar:
# A- Qual é o total gasto na compra.
# B- Quantos produtos custam mais de R$1000.
# C- Qual é o nome do produto mais barato.

t = 0
mil = 0
barato = ''
barato1 = 0
cont = 1
print('--- Bem-Vindo ao Leo Lojas ---')
while True:
    n = str(input('Digite o nome do produto: '))
    p = float(input('Digite o valor do produto: R$'))

    t += p
    if p >= 1000:
        mil += 1
    if cont == 1:
        barato = n
        barato1 = p
    elif barato1 > p:
        barato = n
        barato1 = p

    cont += 1
    d = ''
    while d != 'S' and d != 'N':
        d = str(input('Deseja continuar [S/N]: ')).upper()
    if d == 'N':
        break
print('Obrigado por comprar conosco!')
print(f'''O total da compra: {t}.
Total de produtos acima de mil reais: {mil}.
O produto mais barato foi: {barato}, custando {barato1}''')

# No vídeo de resolução ele apagou o elif e colocou junto ao if com o operador lógico OR.