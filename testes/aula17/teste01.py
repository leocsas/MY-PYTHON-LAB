n = [2, 4, 9, 1]
n[2] = 3 # Muda o número que está na posição 2
n.append(7) # Adiciona o 7
n.sort(reverse=True) # Coloca em ordem decrescente
n.insert(2,0) # Adiciona o 0 na posição 2
n.pop(2) # Elimina o que está na posição 2
n.remove(2)
# Para remover um número sem ter a certeza que ele está na lista:
if 5 in n:
    n.remove(5)
else:
    print('Não encontrei o número 5.')

print(n)
print(f'Essa lista tem {len(n)} elementos.')