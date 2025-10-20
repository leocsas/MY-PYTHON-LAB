# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

v = []

for c in range(0, 5):
    v.append(int(input('Insira um valor: ')))

print(f'O maior valor é {max(v)} na posição: ', end='')
for pos, c in enumerate(v):
    if c == max(v):
        print(f'{pos}... ', end='')

print(f'\nO menor valor é {min(v)} na posição: ', end='')
for pos, c in enumerate(v):
    if c == min(v):
        print(f'{pos}...', end='')