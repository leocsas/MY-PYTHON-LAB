# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual seu salário? '))

sal1 = sal * 1.10
sal2 = sal * 1.15

if sal > 1250:
    print(f'Seu aumento é de 10%. Seu salário atual é {sal1:.2f}')
else:
    print(f'Seu aumento é de 15%. Seu salário atual é {sal2:.2f}')