# Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.

pre = float(input('Digite o valor do produto: '))
desc = pre * (0.95)

# desc = pre - (pre * 5 / 100) # Maneira mostrada na resolução pós realização do meu exercício

print(f'O valor com o desconto de 5% é: {desc:.2f}')