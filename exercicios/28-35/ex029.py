# Escreva um programa que leia a velocidade de um carro.
# Se ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Insira quantos km de velocidade o carro estava: '))
calc = (vel - 80) * 7

if vel > 80:
    print(f'Você foi multado. Sua multa é de R${calc}')