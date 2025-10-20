# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

v = []
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    if n not in v:
        v.append(n)
    r = str(input('Deseja continuar [S/N]: ')).upper()

v.sort()
print(v)