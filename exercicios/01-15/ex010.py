# Crie um programa que leia quanto dinheiro uma pessoa têm na carteira e mostre quantos dólares ela pode comprar.
# Dólar dia 03/10/2025: 5,35

valor = float(input('Insira o valor que você tem: R$'))

dolar = valor / 5.35

print(f'Você pode comprar aproximadamente: U$ {dolar:.2f}')