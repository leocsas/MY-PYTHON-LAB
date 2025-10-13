# Crie um programa que leia vários números inteiros pelo teclado. No final da executão, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

p = 'S'
s = 0 
cont = 0
media = 0
maior = 0
menor = 0

while p == 'S':
    r = int(input('Digite um valor para soma: '))
    s += r
    cont += 1
    p = str(input('Deseja continuar [S/N]: ')).upper()
    if cont == 1:
        maior = menor = r
    else:
        if maior < r:
            maior = r
        if menor > r:
            menor = r

media = s / cont

print(f'A soma dos números: {s}')
print(f'A média deles: {media:.2f}')
print(f'O maior número é {maior} e o menor é {menor}.')

# No vídeo de resolução ele colocou todas as variáveis juntas na mesma linha -> s = cont = media = maior = menor = 0