# Faça um programa que leia um número qualquer a mostra o seu fatorial.
# Ex: 5! = 120

n = int(input('Digite o número para ver seu fatorial: '))
f = 1

while n > 0:
    f *= n
    n -= 1

print(f'O fatorial é: {f}')

# Para utilizar a biblioteca de Math -> factorial(n)