# Faça um programa que leia três números e mostre qual deles é o maior.

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

n1M = n1 > n2 and n3
n2M = n2 > n1 and n3
n3M = n3 > n1 and n2

if n1M == True:
    print(f'O número {n1} é o maior número.')
elif n2M == True:
    print(f'O número {n2} é o maior.')
else:
    print(f'O número {n3} é o maior.')

# No vídeo de resolução ele utiliza:

''' maior = a
if b > and b > c:
    maior = b
if c > a and c > b:
    maior = c  '''