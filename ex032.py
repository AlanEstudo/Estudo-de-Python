# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto

ano = int(input('Digite o ano : '))
calculo = ano % 4 and ano % 100 != 0 or ano % 400 == 0

if calculo == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
