# Desenvolva um programa que leia um número inteiro e diga se ele é ou não um numero primo

n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[033m', end='')
        tot += 1
    else:
        print('\033[034m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot ==2:
    print('É primo!!')
else:
    print('Não é primo!!')


