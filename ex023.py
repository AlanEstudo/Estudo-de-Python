# Faça um programa que leia um numero de 0 a 9999 e mostre na tela
# cada um dos digitos separados.

vlnumero = int(input('Digite um número: '))
u = vlnumero // 1 % 10
d = vlnumero // 10 % 10
c = vlnumero // 100 % 10
m = vlnumero // 1000 % 10
print('Analisando o número {}'.format(vlnumero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))