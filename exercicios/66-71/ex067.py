# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número for solicitado for negativo.

v = 1

while True:
    n = int(input('Digite o valor para tabuada [Negativo para parar]: '))
    if n < 0:
        print('Volte sempre!')
        break
    while v < 11:
        mult = n * v
        print(f'{n} X {v} = {mult}')
        v += 1
    v = 1