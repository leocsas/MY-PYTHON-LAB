# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 50 anos.

idade = 0
maisVelho = 0
nomeVelho = ''
mulheres = 0

for c in range(1, 5):
    n = str(input(f'Insira o nome da {c}º pessoa: '))
    i = int(input(f'Insira a idade da {c}º pessoa: '))
    s = str(input(f'O sexo da {c}º pessoa é masculino ou feminino: ')).lower()
    idade = idade + i
    if c == 1 and s == 'masculino':
        maisVelho = i
        nomeVelho = n
    elif maisVelho < i and s == 'masculino':
        maisVelho = i
        nomeVelho = n

    if s == 'feminino' and i < 50:
        mulheres += 1

media = idade / c
print(f'A média de idade do grupo é {media}.')

if maisVelho == 0:
    print('Não existem homens na lista.')
else:
    print(f'O homem mais velho do grupo  se chama {nomeVelho} tem {maisVelho} anos.')

if mulheres == 0:
    print('Não existem mulheres abaixo de 50 anos')
else:
    print(f'Tem {mulheres} mulheres abaixo de 50 anos.')
