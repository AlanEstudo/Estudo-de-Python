# Crie um programa que vai gera cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor eo maior valor que estão na tupla.

from random import randint
menor = maior = 0

numeros_aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for c in numeros_aleatorios:
    print(f' {c}', end='')
numeros_ordem = sorted(numeros_aleatorios)
for c in numeros_ordem:
    menor = numeros_ordem[0]
    maior = numeros_ordem[4]

print(f'\nO número menor é {menor} e o numero maior é {maior}')
