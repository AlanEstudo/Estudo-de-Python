maior = manor = 0
lista_numeros = []
for posicao in range(0, 5):
    lista_numeros.append(int(input(f'Digite o valor para a posição {posicao}:')))
    if posicao == 0:
        maior = menor = lista_numeros[posicao]
    else:
        if lista_numeros[posicao] > maior:
            maior = lista_numeros[posicao]
        if lista_numeros[posicao] < menor:
            menor = lista_numeros[posicao]
print('=-' * 50)
print(f'Você digitou os valores {lista_numeros}')
print(f'O maior valor digitado foi {max(lista_numeros)} nas posiçoes ', end='')
for i, v in enumerate(lista_numeros):
    if v == maior:
      print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(lista_numeros)} nas posiçoes ', end='')
for i, v in enumerate(lista_numeros):
    if v == menor:
      print(f'{i}... ', end='')
