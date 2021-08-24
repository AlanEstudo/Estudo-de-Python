# Faça um programa que leia uma frase pelo teclado e mostre :
# Quantas vezes parace a letra "A"
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

vlFrase = str(input('Digite uma Frase: ')).strip().upper()

print('A letra "A" aparece {} vezes'.format(vlFrase.count('A')))
print('A Primeira posição é {}'.format(vlFrase.find('A')+1))
print('A última posição é {}'.format(vlFrase.rfind('A')+1)
