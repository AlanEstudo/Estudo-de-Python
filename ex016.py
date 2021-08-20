#Crie um programa que leia um numero Real qualquer pelo teclado e mostra na tela a sua porção inteira
from math import trunc
vlNumero = float(input('Digite um numero Real: '))
#print('Poção inteira de {} é {}'.format(vlNumero,int(vlNumero)))
print('Porção inteira de {} é {}'.format(vlNumero, trunc(vlNumero)))