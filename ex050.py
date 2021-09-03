# Desenvolva um programa que leia seis números inteiros e mostra a soma apenas daqueles que foram pares,
# Se o valor digitado for impar, desconsidere-o
soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}º numero: '.format(c)))
    if n % 2 == 0:
        soma = n + soma
print('A soma de todos os numeros pares é: {}'.format(soma))

