# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0.
# Com uma pausa de 1 segunda entre elas

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM!')