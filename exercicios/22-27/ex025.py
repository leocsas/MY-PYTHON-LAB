# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input('Insira seu nome completo: '))
low = nome.lower()

print('silva' in low)