# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]
v = 0

for n in range(0, 7):
    v = int(input('Insira um número: '))
    if v % 2 == 0:
        valores[0].append(v)
    else:
        valores[1].append(v)

valores[0].sort()
valores[1].sort()
print(f'Os valores pares são {valores[0]}.')
print(f'Os valores ímpares são {valores[1]}.')