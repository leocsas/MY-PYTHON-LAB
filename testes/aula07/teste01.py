n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro valor:"))

# print(f"A soma vale {n1 + n2}")

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f"A soma é {s}. A multiplicação é {m}.", end=' ') # O (end=' ') faz a linha continuar com o próximo print

print(f"A divisão é {d:.3f}.") # Para definir a quantidade de casas decimais que aparecerá é ":.3f" (3 casas decimais.).

print(f"A divisão inteira é {di}.\nA potência é {e}") # O "\n" é para quebrar a linha