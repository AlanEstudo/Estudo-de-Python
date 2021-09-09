# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usúario se ele que ou não continuar a digitar os valores.

continuar = 'S'
media = cont = soma = maior = menor = 0

while continuar != 'N':
    num = int(input('Digite um valor: '))
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        num > maior
        maior = num
    if num < menor:
        menor = num
    soma += num
    continuar = str(input('Continuar a digitar os valores? [S]SIM ou [N]NÃO: ')).upper().strip()[0]
    while continuar !='S' and continuar != 'N':
        print('Opção invalida! ')
        continuar = str(input('Continuar a digitar os valores? [S]SIM ou [N]NÃO: ')).upper().strip()
media = soma / cont
print('Você digitou {} numeros, a médias entre todos os valores digitados é {}'.format(cont, media))
print('O maior valor digitado foi {} e o menor é {}'.format(maior, menor))
print('Fim do programa!')