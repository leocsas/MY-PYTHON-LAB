nome = str(input('Qual o seu nome? '))

if nome == 'Leonardo':
    print('Que nome bonito!')

elif nome == 'Pedro' or 'Maria' or 'Paulo':
    print('Seu nome é popular.')

elif nome in 'Ana Claudia Juliana':
    print('Seu nome é feminino')

else:
    print('Seu nome é comum')

print('Tenha um ótimo dia!')

# Estrutura condicional aninhada.