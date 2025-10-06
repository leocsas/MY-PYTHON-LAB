# O mesmo professor do desafio anterior quer sortear a ordem de apresentações de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

nome1 = input('Insira o nome do primeiro aluno: ')
nome2 = input('Insira o nome do segundo aluno: ')
nome3 = input('Insira o nome do terceiro aluno: ')
nome4 = input('Insira o nome do quarto aluno: ')

sorteio = nome1, nome2, nome3, nome4

print('A ordem das apresentações é: ', random.sample(sorteio, 4))

# O móodulo utilizado no vídeo de resolução foi shuffle