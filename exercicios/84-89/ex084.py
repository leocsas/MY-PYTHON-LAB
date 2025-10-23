# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A- Quantas pessoas foram cadastradas.
# B- Uma listagem com as pessoas mais pesadas.
# C- Uma listagem com as pessoas mais leves.

pessoas = []
mai = men = 0

while True:
    cop = []
    cop.append(str(input('Nome: ')))
    cop.append(float(input('Peso: ')))

    if len(pessoas) == 1:
        mai = men = cop[1]
    else:
        if cop[1] > mai:
            mai = cop[1]
        if cop[1] < men:
            men = cop[1]
        
    pessoas.append(cop[:])

    r = str(input('Deseja continuar [S/N]: ')).upper()
    if r in 'nN':
        break

print(f'Quantidade de pessoas cadastradas:: {len(pessoas)}')
print(f'A pessoa mais pesada foi de {mai}KG. Peso de: ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]} ', end='')

print(f'\nA pessoa mais leve foi {men}KG. Peso de: ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]} ', end='')