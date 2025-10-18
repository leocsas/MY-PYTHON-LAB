# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20.
# Seu programa deverá ler um número pelo teclado de 0 a 20 e mostra-lo por extenso.

cont = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

while True:
    n = int(input('Insira um número de 0 a 20: '))
    if n > 0 and n <= 20:
        print(cont[n])
    else:
        print('Resposta inválida!')
    r = str(input('Deseja continuar [S/N]: ')).upper()
    if r == 'N':
        break
    elif r != 'S':
        print('Resposta inválida.')