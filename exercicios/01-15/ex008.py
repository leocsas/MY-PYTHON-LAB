# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

met = float(input('Insira um valor em metros: '))

cm = met * 100
mm = cm * 10

print(f'O valor inserido em centímetros é: {cm}')
print(f'O valor inserido em mm é: {mm}')