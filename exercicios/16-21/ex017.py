# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenuza.

# Hypot

from math import hypot

catO = float(input('Insira o comprimento cateto oposto: '))
catA = float(input('Insira o comprimento cateto adjacente: '))

# hip = (catO**2 + catA ** 2) ** (1/2)
hip = hypot(catO, catA)

print(f'A hipotenuza é: {hip:.2f}')