# Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50.

for c in range(1, 51, 2):
    c += 1
    print(c)

# No vídeo de resolução ele utilizou if c % 2 == 0
# Também for c in range (2, 51, 2) e o print -> Melhor opção pois economiza o tempo de processamento.