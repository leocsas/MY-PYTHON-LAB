# Crie um programa que leia um número inteiro e mostre se é par ou ímpar.

n = int(input('Insira um número: '))
PI = n % 2

if PI == 1:
    print('Seu número é ímpar.')

else: 
    print('Seu número é par.')