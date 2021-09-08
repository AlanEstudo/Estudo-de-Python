# Melhore o desafio 061,
# Perguntando ao usúario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disse que quer mostrar 0 termos.

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = p
c = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(t), end='')
        t += r
        c += 1
    print('PAUSA')
    mais = int(input('Mostrar mais termos ? ou [0] para sair '))
print('Fim')

