# Desenvolva um programa que leia o primeiro termo ea razão de uma PA.
# No final mostre os 10 primeiros termos dessa progressão

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for c in range(p, d + 1, r):
        print(c, end=' ')
print('Fim')