# Crie um programa que tenha uma tuplas única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista_precos = ('Lápis', 1.50, 'Borracha', 2, 'Caderno', 15.90,
                'Estojo', 25, 'Transferidor ', 4.20, 'Compasso ', 9.99,
                'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for c in range(0, len(lista_precos)):
    if c % 2 == 0:
        print(f'{lista_precos[c]:.<30}', end='')
    else:
        print(f'R${lista_precos[c]:>7.2f}')
print('-' * 40)