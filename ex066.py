# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usúario digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderado o fleg)

soma = cont = 0
while True:
    valor = int(input('Digite um valor: [999] para Sair! '))
    if valor == 999:
        break
    cont += 1
    soma += valor
print(f'Foram digitados {cont} números e a soma é {soma}')

