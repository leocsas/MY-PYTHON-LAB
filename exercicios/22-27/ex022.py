# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas.
# O nome com todas minúsculas.
# Quantas letras ao todo (Sem considerar os espaços).
# Quantas letras tem o primeiro nome

nome = str(input('Insira o seu nome completo: '))

print('Seu nome me maiúsculo é: ', nome.upper())
print('Seu nome me minúsculo é: ', nome.lower())

print('Seu nome têm ', len(nome.replace(' ', '')), 'letras.')
# Usado no vídeo de resolução -> len(nome) - nome.count('0')

sep = nome.split()
print('Seu primeiro nome têm ', len(sep[0]), 'letras.')
# Usado no vídeo de resolução -> nome.find(' ') # Encontra o primeiro espaço e conta os caracteres antes a isso, que seria o primeiro nome.