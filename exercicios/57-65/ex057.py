# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

r = str(input('Digite seu sexo: [M/F] ')).upper()
while r not in 'MF':
    r = str(input('Dados inválidos. Insira novamente:')).upper()
print(f'Seu sexo é {r}.')