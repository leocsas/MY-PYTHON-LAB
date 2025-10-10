# Crie um programa que leia duas notas de aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
# Média abaixo de 5: REPROVADO
# Média entre 5 e 6.9: RECUPERAÇÃO
# Média 7 ou superior: APROVADO

n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print(f'Sua média é {m}. REPROVADO!')
elif m >= 5 and m < 6.9:
    print(f'Sua média é {m}. RECUPERAÇÃO!')
elif m > 7:
    print(f'Sua média é {m}. APROVADO!')
elif m > 10:
    print('Uma das notas está errada!')