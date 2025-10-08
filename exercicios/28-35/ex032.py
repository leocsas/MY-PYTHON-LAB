# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Insira um ano: '))
teste = ano % 4

if teste == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('Esse ano é bissexto.')

else:
    print('Esse ano não é bissexto.')

# No vídeo de resolução importa a data do computador com import datetime from date, utilizando o 0 na resposta.