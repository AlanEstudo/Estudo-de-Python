# Refaça o desafio 051, usando a estrutura while

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = p
c = 1
while c <= 10:
    print('{} -> '.format(t), end='')
    t += r
    c += 1
print('Fim')


