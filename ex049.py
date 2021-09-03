# Refaça o desafio 009, mostrando a tabuada de um número que o usuário esclher, só que agora utilizando um laço for.

n = int(input('Digite um numero: '))
print('-' * 26)

print('Tabuada do {}'.format(n))
for c in range(0, 11):
    print('{} x {}  = {}'.format(n, c, n*c))

print('-' * 26)
