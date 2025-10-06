# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

# SIN, COS, TAN e RADIANS
import math

ang = int(input('Insira o angulo: '))
rad = math.radians(ang)

print(f'O seno do ângulo {ang} é: {math.sin(rad):.2f}')
print(f'O cosseno do ângulo {ang} é: {math.cos(rad):.2f}')
print(f'A tangente do ângulo {ang} é: {math.tan(rad):.2f}')

# Foi necessário pesquisa por fora para verificar o uso do módulo