# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
# Se ele ainda vai ter que se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo de se alistar.

ano = int(input('Em que ano você nasceu'))
idade = 2025 - ano
tempo = 18 - idade
tempoP = idade - 18

if idade < 18:
    print(f'Anos que faltam para o alistamento: {tempo}.')
elif idade == 18:
    print('Está na hora de se alistar.')
elif idade > 18:
    print(f'Se você não se alistou. Anos em atraso : {tempoP}.')

# No vídeo de resolução ele utilizou o import de datetime