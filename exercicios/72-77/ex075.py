# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a- Quantas vezes apareceu o valor 9.
# b- Em que posição foi digitado o primeiro valor 3.
# c- Quais foram os números pares.

um = int(input('Digite o primeiro número: '))
dois = int(input('Digite o segundo número: '))
tres = int(input('Digite o terceiro número: '))
quatro = int(input('Digite o quarto número: '))

t = um, dois, tres, quatro
contP = 0

if t.count(9) > 0:
    print(f'Quantidade de vezes que o número 9 apareceu: {t.count(9)}')

if 3 in t:
    print(f'O primeiro valor de 3 foi digitado na {t.index(3)+1}º posição.')
else:
    print('O número 3 não apareceu nenhuma vez.')

print('Os números pares digitados foram:', end=' ')
for n in t:
    if n % 2 == 0:
        print(n, end=' ')
        contP += 1
if contP == 0:
    print('0')