#Faça um programa que leia o nome de quatro alunos e mostre a orde sorteada
import random
vlA1 = str(input('Primeiro aluno: '))
vlA2 = str(input('Segundo aluno: '))
vlA3 = str(input('Terceiro aluno: '))
vlA4 = str(input('Quarto aluno: '))

vlLista = [vlA1, vlA2, vlA3, vlA4]
random.shuffle(vlLista)

print('Ordem sorteada {}'.format(vlLista))
