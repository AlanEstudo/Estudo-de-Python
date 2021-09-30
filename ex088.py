# Faça um programa que ajuda um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('-' * 40)
print('           JOGO DA MEGA SENA         ')
print('-' * 40)
class_jogo = []
jogos = []

tot = 1
qnt_jogo = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=' * 5, f'SORTEANDO {qnt_jogo} jogos ', f'-=' * 5)
for c in range(0, qnt_jogo):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in class_jogo:
            class_jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    class_jogo.sort()
    jogos.append(class_jogo[:])
    class_jogo.clear()

for indice, lista in enumerate(jogos):
    print(f'jogo {indice + 1}: {lista}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
