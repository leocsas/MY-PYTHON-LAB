# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Júnior
# Até 20 anos: Sênior
# Acima: Master
from datetime import date

hoje = date.today().year
nasc = int(input('Insira o ano que você nasceu: '))
idade = hoje - nasc

if idade <= 9:
    print('Você está na categoria MIRIM!')
elif idade <= 14:
    print('Você está na categoria INFANTIL!')
elif idade <= 19:
    print('Você está na categoria JÚNIOR!')
elif idade <= 25:
    print('Você está na categoria SÊNIOR!')
else:
    print('Você está na categoria MASTER!')