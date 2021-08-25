# Faça um programa que faça o computador "pensa" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário vencer ou perdeu

from random import randrange
vlnumero = int(input('Digite um numero entre 0 e 5: '))
vlPensado= randrange(0, 5)
if vlnumero == vlPensado:
    print('Você venceu!')
else:
    print('Você Perdeu!')
print('Numero Pensado foi {}'.format(vlPensado))