# Escreva um programa que leia um número n inteiro qualquer a mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('Qunatos elementos você quer ver de um sequência de Fibonacci: '))
f1 = 0
f2 = 1
cont = 3
print(f1)
print(f2)

while cont <= n:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3)
    cont+=1