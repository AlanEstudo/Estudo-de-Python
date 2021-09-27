# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# Quantas pessoas foram registrada.
# Uma listagem com as pessoas mais pessadas.
# Uma listagem com as pessoas mais leves.

cadastro = []
pessoas = []
cont_pessoas = maior = menor = 0

while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    pessoas.append(cadastro[:])
    cadastro.clear()
    sair = str(input('Quer continuar : [S/N]')).upper().strip()[0]
    cont_pessoas += 1
    if sair in 'N':
        break
print('=>' * 35)
print(f'Foram cadastradas {cont_pessoas} pessoas.')

print(f'O maior peso foi de {maior}KG. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end=' ')
print()

print(f'O menor peso foi de {menor}KG. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
