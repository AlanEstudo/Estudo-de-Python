# Crie um programa onde o usuário possa digirar vários valores numéricos e cadastre-os em uma lista
# Caso o número já exista lá dentro, ele não será adicionado.
# No final srão exibidos os valores únicos digitados, em orde crescente.

lista_numeros = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista_numeros:
        lista_numeros.append(valor)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não adicionado')
        
    sair = ' '
    while sair not in 'NS':
        sair = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if sair != 'S' and sair != 'N':
            print('Opção invalida!')
    if sair == 'N':
        break
lista_numeros.sort()
print('=-'*35)
print(f'Você digitou os valores {lista_numeros}')
