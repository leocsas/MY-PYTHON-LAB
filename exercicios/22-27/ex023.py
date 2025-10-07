# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

# Ex: Digite um número: 1834
# Unidade
# Dezena
# Centena
# Milhar

n = int(input('Insira um número de 1 a 9999: '))

qt = f'{n:.4f}'
print('Analisando o número: ', n)

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Unidade: ', u)
print('Dezena: ', d)
print('Centena: ', c)
print('Milhar: ', m)
# Revisar