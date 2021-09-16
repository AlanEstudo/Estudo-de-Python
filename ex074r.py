from random import randint
numeros_aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram : ',end='')

for c in numeros_aleatorios:
    print(f'{c}', end=' ')
print(f'\nO menor valor foi {min(numeros_aleatorios)} e o maior valor {max(numeros_aleatorios)}')