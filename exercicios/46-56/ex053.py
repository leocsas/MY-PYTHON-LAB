# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: A torre da derrota.

f = str(input('Verificar se é um políndromo: ')).lower().replace(' ', '')
l = len(f)
t = ''

for c in range(l, 0, -1):
    l = l - 1
    t = t + f[l]
    
if t == f:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')