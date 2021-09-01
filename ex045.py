# Crie um programa que faça o computador jogar Jokenpô com você
# Regras  :  PEDRA X PAPEL = PAPEL
#            PAPEL X TESOURA = TESOURA
#            TESOURA X PEDRA = PEDRA

from random import randint
from time import sleep
vljogada = ('PEDRA', 'PAPEL', 'TESOURA')
print('=' * 10, 'GAME JOKENPÔ', '=' * 10)
print('''Escolha uma opção:
        [0] PEDRA
        [1] PAPEL
        [2] TESOURA''')
vlOpcaoUsuario = int(input('Faça sua Jogada!: '))

print('USUARIO: {}'.format(vljogada[vlOpcaoUsuario]))
vlOpcaoComputador = randint(0, 2)
print('COMPUTADOR : {}'.format(vljogada[vlOpcaoComputador]))

print('=' * 30)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=' * 30)

if vlOpcaoUsuario == 0 and vlOpcaoComputador == 1 or vlOpcaoUsuario == 1 and vlOpcaoComputador == 2 and vlOpcaoUsuario == 2 and vlOpcaoComputador == 0:
    print('Computador VENCEU!')
elif vlOpcaoUsuario == vlOpcaoComputador:
    print('Empate')
else:
    print('Você VENCEU!')

