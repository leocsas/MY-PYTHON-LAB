# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

nome1 = str(input('Insira o nome do primeiro aluno: '))
nome2 = str(input('Insira o nome do segundo aluno: '))
nome3 = str(input('Insira o nome do terceiro aluno: '))
nome4 = str(input('Insira o nome do quarto aluno: '))

sorteio = [nome1, nome2, nome3, nome4]

print(f'Quem irá limpar o quadro é: ', random.choice(sorteio))

# Necessário pesquisa por fora para verificar uso do módulo