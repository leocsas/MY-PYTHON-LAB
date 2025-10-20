galera = []
dado = []

for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Necessário para não apagar as duas listas
    dado.clear()

print(galera)