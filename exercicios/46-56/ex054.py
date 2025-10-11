# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores.

from datetime import date

p1 = int(input('Em que ano a 1º pessoa nasceu? '))
p2 = int(input('Em que ano a 2º pessoa nasceu? '))
p3 = int(input('Em que ano a 3º pessoa nasceu? '))
p4 = int(input('Em que ano a 4º pessoa nasceu? '))
p5 = int(input('Em que ano a 5º pessoa nasceu? '))
p6 = int(input('Em que ano a 6º pessoa nasceu? '))
p7 = int(input('Em que ano a 7º pessoa nasceu? '))

p = p1, p2, p3, p4, p5, p6, p7
ano = date.today().year
maior = 0
menor = 0

for c in range (0 , 7):
    if ano - p[c] >= 18:
        maior += 1
    else:
        menor +=1

print(f'{menor} é a quantidade de pessoas que são menores de idade.')
print(f'{maior} é a quantidade de pessoas que são maiores de idade.')

# No vídeo de resolução ele inseriu o requerimento dentro do for utilizando os valores de range. Também utilizou o else para contar a q