# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

r ='S'
notas = []
pos = 0

while r in 'sS':
    lista = []
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    notas.append(lista[:])
    lista = []
    r = str(input('Deseja continuar [S/N]: '))
    pos += 1

print('Pos.  -   Nome   -   Média')
for n in range(0, pos):
    media = (notas[n][1] + notas[n][2]) / 2
    print(f'{n:^3} {notas[n][0]:<12} {media:>7}')

while True:
    opci = int(input('Qual aluno você deseja ver as notas [999 para interromper]: '))
    if opci == 999:
        break
    if opci <= len(notas) - 1:
        print(f'As notas de {notas[opci][0]} são {notas[opci][1:]}')
print('FIM!')