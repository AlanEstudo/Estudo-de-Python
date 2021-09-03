# Faça um programa que calcule a soma entre todos os numero impares que sao multiplos de tres e que se encontram no intervalor de 1 ate 500.

s = 0
contador = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
                print(c, end=' ')
                s += c
                contador += 1
print('\nA soma de todos os {} valores solicitados é de: {}'.format(contador, s))