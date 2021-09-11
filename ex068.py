# Faça um programa que jogue Par ou Impar com o computador.
# O jogo será interronpido quando o jogador PERDER.
# Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

computador = soma = 0
jogada_jogador = jogada_computador = resultado = sair = ''
print('='*43)
print('=>'*6, 'JOGO PAR OU ÍMPAR', '<='*6)
print('='*43)

while True:
    jogador = int(input('Faça sua jogada ÍMPAR/PAR: '))
    if jogador == int:
        print('Opção Invalida!')
        jogador = int(input('Faça sua jogada ÍMPAR ou PAR: '))

    if jogador % 2 == 0:
        jogada_jogador = 'PAR'
        computador_jogada = 'IMPAR'
    else:
        jogada_jogador = 'IMPAR'
        computador_jogada = 'PAR'
    print('-' * 43)
    print('Computador jogando ...')
    print('-' * 43)
    sleep(1)
    computador = randint(1, 9)
    soma = jogador + computador
    if computador % 2 == 0:
        jogada_computador = 'PAR'
    else:
        jogada_computador = 'IMPAR'
    print(f'Você jogou {jogada_jogador} o numero foi {jogador}')
    print(f'Computador jogou {computador_jogada} e o numero foi {computador}')
    print(f'A soma foi de {soma}')
    print('-'*43)

    if (jogador + computador) % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

    if resultado == jogada_jogador:
        print('GANHOU')
    else:
        print('PERDEU')
        break





