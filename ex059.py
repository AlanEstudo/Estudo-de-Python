# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] soma
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

menu = 4
while menu != 5:
    n1 = float(input('Digite o 1º número: '))
    n2 = float(input('Digite o 2º número: '))
    menu = int(input('''
    ---------- Opção ----------
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa
    '''))
    if menu == 1:
        soma = n1 + n2
        print('Soma entre {} e {} é : {}'.format(n1, n2, soma))
    elif menu == 2:
        multiplicar = n1 * n2
        print('A multiplicação ente {} e {} é : {}'.format(n1, n2, multiplicar))
    elif menu == 3:
        if n1 > n2 :
            print('O maior numero entre {] e {} é {}'.format(n1, n2, n1))
        else:
            print('O maior numero entre {] e {} é {}'.format(n1, n2, n2))

print('Fim do programa!')