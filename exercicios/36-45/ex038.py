# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
elif n1 == n2:
    print('Os números são iguais!')