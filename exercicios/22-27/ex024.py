# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "Santo"

nome = str(input('Insira o nome de uma cidade: '))
separar = nome.split()

print('santo' in separar[0].lower())

# Usado no vídeo de resolção -> cid = str(input('Em que cidade você nasceu? )).strip()
# print(cid[:5].upper() ==  'SANTO)