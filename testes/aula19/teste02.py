pessoas = {'nome': 'Leonardo', 'sexo': 'M', 'idade': 23}

del pessoas['sexo'] # Apaga
pessoas['nome'] = 'Leandro' # Modifica
pessoas['peso'] = 78.5 # Adiciona
for k, v in pessoas.items():
    print(k, ' = ', v)