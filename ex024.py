# Crie um programa que leia o nome de uma cidade e diga se ela começar ou nao com o nome "SANTO"

vlNome = str(input('Cidade: ')).strip()

vlLista = vlNome.split()

print('Começa com o nome SANTOS ? {}'.format('SANTOS' in vlLista[0].upper()))
# print(vlLista[:5].upper() == 'SANTOS')
