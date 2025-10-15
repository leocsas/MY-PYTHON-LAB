# Faça um programa que jogue par ou ímpar com o PC. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
# Solicitar valor, solicitar ímpar ou par, informar qual número foi jogado pelo usuário e pelo computador, sua soma e quem venceu. Mostrar quantidade de vitórias.

import random
v = 0
s = 0

while True:
    numeroPC = random.randint(1, 10)
    aposta = str(input('Par ou Ímpar [P/I]: ')).upper()

    while aposta != 'P' and aposta != 'I':
        aposta = str(input('Inválido, digite novamente [P/I]: ')).upper()

    numero = int(input('Qual sua aposta: '))
    s = numero + numeroPC
    verificar = s % 2
    
    if (aposta == 'P' and verificar == 0) or (aposta == 'I' and verificar == 1):
        print(f'Máquina jogou {numeroPC} e você {numero}.')
        print(f'A soma é: {s}')
        print('Você ganhou!')
        v += 1
    elif (aposta == 'P' and verificar == 1) or (aposta == 'I' and verificar == 0):
        print(f'Máquina jogou {numeroPC} e você {numero}.')
        print(f'A soma é: {s}')
        print('Você perdeu!')
        print(f'Obrigado por jogar, você ganhou {v} vezes.')
        break

# No vídeo de resolução ele inseriu uma linha onde informa se o resultado é par ou impar -> print('Deu par' if s % 2 == 0 else 'Deu ipar')