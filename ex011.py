# Crie um programa que leia a largura e a altura de uma parede em metros, calcula a sua área e a quantidade
# de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

vlAltura = float(input('Qual a altura :'))
vlLargura = float(input('Qual a largura :'))

vlArea = vlAltura * vlLargura
vlQntTin = vlArea / 2

print('Uma parede com {:.2f} m², precisa de {:.2f} Litros Tinta para pintar'.format(vlArea, vlQntTin))