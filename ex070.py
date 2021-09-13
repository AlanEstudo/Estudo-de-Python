# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No fnal mostre:
# Qual é o total gasto na compra.
# quantos produtos custam mais de R$1000.
# Qual é o nome do produto mais barato.
print('=' * 10, 'TooLoja', '=' * 10)
total_compra = produtos_1000 = cont = menor_preco = 0
nome_barato = ''
while True:
    nome_produto = str(input('Nome do produto: ')).strip()
    preco_produto = float(input('Preço do produto:R$ '))
    cont += 1
    total_compra += preco_produto
    if preco_produto > 1000:
        produtos_1000 += 1
    if cont == 1 or preco_produto < menor_preco:
        menor_preco = preco_produto
        nome_barato = nome_produto

    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if sair == 'N':
        break
print('-' * 10, 'Resumo da compra', '-' * 10)
print(f'Total da compra: R${total_compra:.2f}')
print(f'Foram {produtos_1000} com mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato}que custa R${menor_preco:.2f}')
