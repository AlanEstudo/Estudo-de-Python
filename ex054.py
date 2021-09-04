# Crie um programa que leia o ano de nascimento de sete pessoas.
# Mostre quantas pessoas ainda nao atingiram a maioridade,
# Quantoas pessoas ja são maiores

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    vlNascimento = int(input('Digite o {}º ano de nascimento: '.format(c)))
    if atual - vlNascimento < 21:
        menor += 1
    else:
        maior += 1
print('{} pessoas ainda não atingiram maioridade e {} já são maiores de idade'.format(menor, maior))

