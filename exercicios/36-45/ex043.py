# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu resultado de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ieal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))

imc = peso / altura ** 2

if imc < 18.5:
    print(f'Seu imc é {imc:.2f}, você está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu imc é {imc:.2f}, você está com o peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu imc é {imc:.2f}, você está com sobrepeso.')
elif imc >= 30 and imc <= 40:
    print(f'Seu imc é de {imc:.2f} você está com obesidade.')
elif imc > 40:
    print(f'Seu imc é {imc:.2f}, você está com obesidade mórbida.')