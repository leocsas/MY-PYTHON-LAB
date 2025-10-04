# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

teste = input("Digite algo para teste: ")

print(f"O tipo desse valor é {type(teste)}")

print("É um número?", teste.isnumeric()) # = Número

print("É uma letra?", teste.isalpha()) # = Letra

print("É um número e/ou letra?", teste.isalnum()) # = Número e/ou letra

print("Está em maiúsculo?", teste.isupper()) # Confere se o que está escrito está em maiúscula

print("Está em minúsculo?", teste.islower()) # Confere se o que está escrito está em minúsculo

print("Está capitalizada?", teste.istitle()) # Confere se o que está escrito está capitalizada (maiúsculo e minúsculo)

print("Só tem espaço?", teste.isspace()) # Confere se só foi inserido espaços