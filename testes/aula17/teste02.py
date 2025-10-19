valores = []

valores.append(5)
valores.append(7)
valores.append(9)
valores.append(4)

print(valores)

for c, v in enumerate(valores): # Enumerate pega o valor e chave.
    print(f'Na posição {c}, encontrei o valor {v}!')