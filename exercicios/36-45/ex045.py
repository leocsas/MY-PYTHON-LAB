# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

escolha = input('Pedra, papel ou tesoura? ')
pessoa = escolha.upper()
maq1 = 'PEDRA', 'PAPEL', 'TESOURA'
maq = random.choice(maq1)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('...')
sleep(2)

if (pessoa == 'PEDRA' and maq == 'PAPEL') or (pessoa == 'PAPEL' and maq == 'TESOURA') or (pessoa == 'TESOURA' and maq == 'PEDRA'):
    print(f'Eu escolho {maq}!')
    print('Eu ganhei, tente novamente.')
elif (maq == 'PEDRA' and pessoa == 'PAPEL') or (maq == 'PAPEL' and pessoa == 'TESOURA') or (maq == 'TESOURA' and pessoa == 'PEDRA'):
    print(f'Eu escolho {maq}.')
    print('você ganhou!')
elif maq == pessoa:
    print(f'Eu escolho {maq}!')
    print('Empatou. Tente novamente.')
else:
    print('Opção inválida!')

# Idéia da "animação" do Jokenpo pega no vídeo de resolução!