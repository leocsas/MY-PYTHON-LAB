# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
v = 10
cont = 0

while v > 0:
    while v > 0:
        print(t)
        t += r
        v -= 1
        cont += 1
    v = int(input('Quantos termos você deseja ver a mais: '))

print(f'Foram mostrados {cont} termos.')