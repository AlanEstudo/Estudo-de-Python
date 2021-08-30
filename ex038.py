# Escreva um programa que leia dois números inteiros ecompare-os,mostrando na tela uma mensegem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

vlN1 = int(input('Digite o primeiro número: '))
vlN2 = int(input('Digite o segundo número: '))

if vlN1 > vlN2:
    print('O primeiro número é maior!')
elif vlN2 > vlN1:
    print('O segundo número é maior!')
elif vlN1 == vlN2 or vlN2 == vlN1:
    print('Não existe valor maior, os dois são iquais!')