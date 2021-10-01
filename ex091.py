# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionario. No final, coloque em ordem,
# Sabendo que o vencedor tirou o maior número.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = list()
jogadores["Jogador1"] = randint(1, 6)
jogadores["Jogador2"] = randint(1, 6)
jogadores["Jogador3"] = randint(1, 6)
jogadores["Jogador4"] = randint(1, 6)

print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'   O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f'  {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)