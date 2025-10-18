# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

s = randint(0, 10), randint(0,10), randint(0, 10), randint(0, 10), randint(0, 10)

print(f'Os números gerados foram {s}')
print(f'O maior número foi {max(s)}')
print(f'O menor número foi {min(s)}')