# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.

valores_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
                   'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                   'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
                   'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continuar = ''
while continuar != 'N':
    while True:
        numero_usuario = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero_usuario <= 20:
            break
        print('Numero incorreto! ', end='')

    print(f'Você digitou o número {valores_extenso[numero_usuario]}')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]


