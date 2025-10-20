galera = []
dado = []
mai = men = 0

for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Necessário para não apagar as duas listas
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        mai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        men += 1

print(f'Temos {mai} maiores de idade. Temos {men} menores de idade.')