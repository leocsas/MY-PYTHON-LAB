# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Foi utilizado 35 anos como tempo minimo de contribuição, visto que no ano do vídeo eram essas as regras.

from datetime import date
usuario = {}

usuario['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
usuario['idade'] = date.today().year - ano
usuario['carteira'] = int(input('Carteira de trabalho (0 se não tem): '))

if usuario['carteira'] != 0:
    usuario['contrato'] = int(input('Ano de contratação: '))
    usuario['salario'] = float(input('Salário: R$'))
    usuario['aposentadoria'] = (usuario['contrato'] + 35) - ano

for d, v in usuario.items():
    print(f'{d} tem valor de: {v}')