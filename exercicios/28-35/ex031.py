# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

viagem = int(input('Quantos Km será a viagem: '))

if viagem > 200:
    print('Sua viagem custará', viagem * 0.50, '!')

else:
    print('Sua viagem custará', viagem * 0.45, '!')

# Poderia ter sido criadas variáveis para o calculo.