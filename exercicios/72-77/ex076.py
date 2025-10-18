# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na senquência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

p = 'Notebook', 2400, 'Teclado', 60, 'Mouse', 40, 'Monitor', 850, 'Cabos', 100, 'Extensão', 42, 'Fone', 50, 'Microfone', 36

for n in range(0, len(p)):
    if n % 2 == 0:
        print(f'{p[n]:.<30}', end=' ')
    elif n % 2 == 1:
        print(f'R${p[n]:>9.2f}')