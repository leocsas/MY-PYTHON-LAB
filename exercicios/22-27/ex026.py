# Faça um programa que leia uma frase pelo teclado e mostre

# Quantas vezes aparece a letra "A".
# Em que posição ela aparece pela primeira vez.
# Em que posição ela aparece pela última vez

nome = str(input('Insira uma frase: '))
lower = nome.lower()

print('A letra "a" aparece', lower.count('a'), 'vezes na frase')

print('A primeira letra "a" aparece na posição ', lower.find('a') + 1)
print('A última letra "a" aparece na posição ', lower.rfind('a') + 1)

# No vídeo de resolução ele utilizou '.strip()' para acabar com os espaços antes da frase, caso coloquem não afetar a posição