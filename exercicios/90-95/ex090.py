# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
historico = {}
historico['nome'] = str(input('Nome: '))
historico['media'] = float(input('Média: '))

if historico['media'] >= 5:
    historico['situação'] = 'Aprovado'
else:
    historico['situação'] = 'Reprovado'

print(f'Nome: {historico['nome']}')
print(f'Sua média: {historico['media']}')
print(f'Sua situação: {historico['situação']}')

# No vídeo de resolução ele utilizou o for para imprimir no terminal:
#   for k, v in aluno.items():
#       print(f' -{k} é igual a {v}')'