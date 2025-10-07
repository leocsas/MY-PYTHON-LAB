# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = str(input('Insira o seu nome completo: '))
sep = nome.split()

print('Seu primeiro nome é: ', sep[0])
print('Seu último nome é: ', sep[-1])

# Usado no vídeo de resolução -> nome[len(nome)-1]