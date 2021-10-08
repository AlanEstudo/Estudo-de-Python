# Crie um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular(largura e comprimento)
# e mostre a area do terreto.

def calculo_area(largura, comprimento):
    area = largura * comprimento
    print(f'A area de um terreno {largura} x {comprimento} é de {area}m².')

# Programa principal
print(' Controle de Terrenos')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

calculo_area(largura, comprimento)
