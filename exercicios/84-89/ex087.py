# Aprimore o desafio anterior, mostrando no final: 
# A- A soma de todos os valores pares digitados.
# B- A soma dos valores da terceira coluna.
# O- maior valor da segunda linha.

m = [[], [], []]
pares = 0
terceira = 0
maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        m[linha].append(int(input(f'Insira valor para [{linha}, {coluna}]: ')))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{m[linha][coluna]:^5}]', end='')
        if m[linha][coluna] % 2 == 0:
            pares += m[linha][coluna]
        if coluna == 0:
            maior = m[1][coluna]
        elif m[1][coluna] > maior:
            maior = m[1][coluna]
    terceira += m[linha][2]

        
    print()

print(f'Soma dos pares: {pares}.')
print(f'O maior valor da segunda linha: {maior}.')
print(f'Soma dos valores da terceira coluna: {terceira}.')