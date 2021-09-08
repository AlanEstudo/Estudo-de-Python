# faça um programa que leia um número qualquer e mostre o sei fatorial.
# ex: 5! = 5x4x3x2x1 = 120

n = int(input('Digite um valor: '))
c = n
soma = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    soma *= c
    c -= 1
print(soma)