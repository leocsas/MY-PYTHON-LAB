nome = 'Leonardo'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7m'
        }

print(f'Olá {cores['pretoebranco']}{nome}{cores['limpa']}')