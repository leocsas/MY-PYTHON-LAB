# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la. Sabendo que a cada litro de tinta, pinta uma área de 2m quadrados.

lar = float(input('Insira a largura: '))
alt = float(input('Insira a altura: '))

area = lar * alt

tinta = area / 2

print(f"A quantidade de tinta necessária é: {tinta} Litros.")