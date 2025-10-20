teste = []
teste.append('Leonardo')
teste.append(23)
galera = []

galera.append(teste[:]) # Cópia
teste[0] = 'Geovanna'
teste[1] = 20
galera.append(teste)
print(galera)