# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

v = []
r = 'S'
p =[]
i = []

while r == 'S':
    v.append(int(input('Insira um valor: ')))
    r = (str(input('Deseja continuar [S/N]: '))).upper()

for c in v:
    if c % 2 == 0:
        p.append(c)
    else:
        i.append(c)

print(f'Os valores inseridos foram: {v}')
print(f'Os valores pares inseridos foram: {p}')
print(f'Os valores ímpares inseridos foram: {i}')