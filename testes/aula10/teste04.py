n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print(f'A nota média foi {m:.2f}')

if m >= 5:
    print('Parabéns, você passou!')
else:
    print('Estude mais.')