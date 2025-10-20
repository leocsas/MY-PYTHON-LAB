#  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A- Quantos números foram digitados.
# B- A lista de valores, ordenada de forma decrescente.
# C- Se o valor 5 foi digitado e está ou não na lista.

v = []
r = 'S'
while r == 'S':
    v.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar [S/N]: ')).upper()

print(f'Foram digitados {len(v)} números.')
v.sort(reverse=True)
print(v)

if 5 in v:
    print('Existe um valor 5 na lista.')
else:
    print('Não existe 5 na lista.')