#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa qe ajude ele, lendo o nomde deles e escrevendo o nome do escolhido
#

from random import choice
vlA1 = input('Digite o primeiro nome: ')
vlA2 = input('Digite o segundo nome: ')
vlA3 = input('Digite o terceiro nome: ')
vlA4 = input('Digite o quarto  nome: ')

vlLista = [vlA1, vlA2, vlA3, vlA4]
vlEscolhido = choice(vlLista)

print('O escolhido foi {} '.format(vlEscolhido))