# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o Flag = 999).

s = 0
cont = 0
n = int(input('Digite um valor para somar: '))

while n != 999:
    s += n
    cont +=1
    n = int(input('Digite um valor para somar [999 para parar]: '))

print(f'Você digitou {cont} números e a soma entre eles é {s}.')