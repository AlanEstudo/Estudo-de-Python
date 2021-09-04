# faça um programa que leia o peso de cinco pessoas.
# Mostre qual foi o maior e o menos peso lidos

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(c)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {:.2f}, e o menor foi {:.2f}'.format(maior, menor))

