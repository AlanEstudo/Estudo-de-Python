# Crie um programa onde o usùario possa digitar cinco valores numéricos
# Cadastre-os em uma lista, já na posição correta de inserção(Sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista_numeros = []
for cont in range(0, 5):
    valor = int(input('Digite o  valor: '))
    if cont == 0 or valor > lista_numeros[-1]:
        lista_numeros.append(valor)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista_numeros):
            if valor <= lista_numeros[pos]:
                lista_numeros.insert(pos, valor)
                break
            pos += 1
print(f'Os números digitados foram {lista_numeros}')
