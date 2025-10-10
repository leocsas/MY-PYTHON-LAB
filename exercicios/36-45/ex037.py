# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para o binário
# 2 para octal
# 3 para hexadecimal

n = int(input('Insira um número: '))
base = int(input('Qual a base de conversão? Escreva "2" para binário, "8" para octal e "16" para hexadecimal: '))

if base == 2:
    print(f'A base binária do número {n} é {bin(n)}.')
elif base == 8:
    print(f'A base octal do número {n} é {oct(n)}.')
elif base == 16:
    print(f'A base hexadecimal do número {n} é {hex(n)}.')
else:
    print('Base não encontrada, escreva o número certo para base de conversão.')