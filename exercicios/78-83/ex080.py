# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

v = []
pos = 0

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > v[-1]:
        v.append(n)
        print('Adicionado ao final da lista.')
    else:
        while pos < len(v):
            if n <= v[pos]:
                v.insert(pos, n)
                print(f'Adicionado na posição {pos}.')
                break
            pos += 1

print(v)