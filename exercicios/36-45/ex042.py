# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes

a = int(input('Insira os cm da primeira linha: '))
b = int(input('Insira os cm da segunda linha: '))
c = int(input('Insira os cm da terceira linha: '))
trian = ((a < (b + c)) and (b < (a + c)) and (c < (a + b))) or a == c and a == b

if trian == True and (a == b and a == c):
    print('Seu triângulo é um equilátero.')
elif trian == True and ((a == b or a == c) or b == c):
    print('Seu triângulo é um Isóceles.')
elif trian == True and (a != b and b != c and a != c):
    print('Seu triângulo é um escaleno!')
else:
    print('Não é possível formar um triângulo.')