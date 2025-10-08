# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Quantos cm tem o comprimento da primeira linha: '))
b = float(input('Quantos cm tem o comprimento da segunda linha: '))
c = float(input('Quantos cm tem o comprimento da terceira linha: '))

if a < b + c and b < a +c and c < a + b:
    print('Os valores podem formar um triângulo.')
else:
    print('Os valores não podem formar um triângulo.')