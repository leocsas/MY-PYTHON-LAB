a = [2, 4, 7, 9]
b = a
b[2] = 0

print(a)
print(b)
# O PYTHON cria uma ligação entre listas

# Para criar um cópia para alteraçõa:
c = [2, 4, 7, 9]
d = c[:] # Todos os números.
d[2] = 0
print(c)
print(d)