# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

p = ('Sol', 'Montanha', 'Livro', 'Chave', 'Rio', 'Janela', 'Relógio', 'Caneta')

for n in p:
    print(f'\n{n} tem as seguintes vogais:', end=' ')
    if 'a' in n:
        print('a', end=' ')
    if 'e' in n:
        print('e', end=' ')
    if 'i' in n:
        print('i', end=' ')
    if 'o' in n:
        print('o', end=' ')
    if 'u' in n:
        print('u', end=' ')