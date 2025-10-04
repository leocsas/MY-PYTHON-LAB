# Escreva um programa que pergunte a quantidade de Km pecorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmPer = float(input('Insira quantidade de Km rodados: '))
dias = int(input('Insira quantidade de dias que o carro foi alugado: '))

total = (dias * 60) + (kmPer * 0.15)

print(f'O total a pagar é: R${total:.2F}')