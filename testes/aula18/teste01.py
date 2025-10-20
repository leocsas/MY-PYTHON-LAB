teste = []
teste.append('Leonardo')
teste.append(23)
galera = []

# Teste para mostrar que as listas estão ligadas, para fazer uma cópia se utiliza o [:]
galera.append(teste)
teste[0] = 'Geovanna'
teste[1] = 20
galera.append(teste)
print(galera)