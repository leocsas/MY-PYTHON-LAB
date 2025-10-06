# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira

# Exemplo: quando gitiar 6.752, a parte inteira é 6

from math import trunc

pi = float(input('DIgite um número para vermos sua porção maior: '))

print(f'A porção inteira do número {pi} é:', trunc(pi))

# Outro método para isso é o float e o int