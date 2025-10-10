# Escreva um programa que aprove um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

emp = float(input('Qual o valor da casa: R$'))
sal = float(input('Qual o seu salário: R$ '))
anos = int(input('Em quantos anos: '))

meses = anos * 12
prest = emp / meses
prct = prest / sal * 100

if prct > 30:
    print(f'Para pagar uma casa de R${emp} em {anos} anos, a prestação será de {prest:.2f}. Empréstimo negado.')
else:
    print(f'Para pagar uma casa de R${emp} em {anos} anos, a prestação será de {prest:2f}. Empréstimo aprovado.')