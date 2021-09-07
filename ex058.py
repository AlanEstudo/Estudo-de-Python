# Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entra 0 e 10.
# Só que agora o jogador vai tentar adivinha até acertar, mostrando no final quantas palites fora necessários para vencer

from random import randint
vlComputador = randint(0, 10)
print('Computador pensou em um numero tente adivinhar!')
vlJogador = int(input(' Qual o numero? : '))
cont = 1
while vlJogador != vlComputador:
    vlJogador = int(input('Tente novamente: '))
    cont += 1
print('Acertou!, foram {} jogadas'.format(cont))

