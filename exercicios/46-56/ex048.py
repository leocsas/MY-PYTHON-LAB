# Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 e 500.
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        s += c
print(s)

# No vídeo de resolução ele utilizou um contador -> cont = 0 -> cont = cont + 1, dentro do if