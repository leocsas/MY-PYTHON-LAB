# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# A- Quantas pessoas tem mais de 18 anos.
# B- Quantos homens foram cadastrados
# C- Quantas mulheres tem mais de 20 anos.
# Cadastre pessoa, solo=icitar idade e sexo e perguntar se deseja continuar [S/N]. Caso tenha colocado valor errado perguntar novamente.
# Mostrar valores pedidos.

maior = 0
homens = 0
mulheres = 0

while True:
    print('--- CADASTRAR PESSOA ---')
    i = int(input('Digite a idade da nova pessoa: '))
    s = str(input('Digite seu sexo [M/F]: ')).upper()

    if i > 17:
        maior += 1
    if s == 'M':
        homens += 1
    if s == 'F' and i > 20:
        mulheres += 1

    d = str(input('Deseja continuar [S/N]: ')).upper()
    while d != 'N' and d != 'S':
        d = str(input('Insira corretamente. Deseja continuar [S/N]: ')).upper()
    if d == 'N':
        break

print(f'Quantidade de pessoas maiores de idade: {maior}')
print(f'Quantidade de homens cadastrados: {homens}')
print(f'Quantidade de mulheres acima de 20 anos: {mulheres}')

# No vídeo de resolução ele colocou o s dentro de um while para ter certeza que o usuário irá digitar corretamente, assim como realizado na variável 'd'