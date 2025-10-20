# Crie um programa onde o usuário digite uma expressão númerica qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

n = str(input('Digite uma expressão numérica: '))
e = []

for c in n:
    if c == '(':
        e.append('(')
    elif c == ')':
        if len(e) > 0:
            e.pop()
        else:
            e.append(')')
            break

if len(e) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')