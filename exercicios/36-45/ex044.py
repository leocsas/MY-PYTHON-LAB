# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# À vista dinhiero/PIX: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Qual o valor dor produto? R$'))
pag = int(input('''Qual a forma de pagamento?
[1] Dinheiro
[2] Pix
[3] Cartão à vista
[4] Cartão em 2x
[5] Cartão 3x ou mais

INSIRA AQUI: '''))

if pag == 1 or pag == 2:
    rec = valor * 0.90
    print(f'Você ganhou um desconto de 10%. Valor total é: R${rec}.')
elif pag == 3:
    rec = valor * 0.95
    print(f'Você ganhou um desconto de 5%. Valor toral é: R${rec}.')
elif pag == 4:
    print(f'O preço total é: R${valor}.')
elif pag == 5:
    rec = valor * 1.20
    print(f'Essa opção tem 20% de juros. Valor total é: R${rec}.')
else:
    print('Digite as informações corretamente.')