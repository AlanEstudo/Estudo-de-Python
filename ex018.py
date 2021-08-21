#Faca um programa que lei um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import asin, cos, tan, radians
vlAngulo = float(input('Digite o valor do ângulo: '))

vlSeno = asin(radians(vlAngulo))
vlCossen = cos(radians(vlAngulo))
vlTangente = tan(radians(vlAngulo))

print('O Seno do valor {} é {:.2f} '.format(vlAngulo, vlSeno))
print('O Cosseno do valor {} é {:.2f} '.format(vlAngulo, vlCossen))
print('A Tangente do valor {} é {:.2f} '.format(vlAngulo, vlTangente))