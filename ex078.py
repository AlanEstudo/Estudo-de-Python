# faça um programa que leia 5 valores numéricos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista

lista_numeros = []
for posicao in range(0, 5):
        lista_numeros.append(int(input(f'Digite o valor para a posição {posicao}:')))
maior = max(lista_numeros)
menor = min(lista_numeros)
posicao_maior= []
posicao_menor= []
for pos, val in enumerate(lista_numeros):
        if val == maior:
                posicao_maior.append(pos)
        if val == menor:
                posicao_menor.append(pos)

print('=-' * 50)
print(f'Você digitou os valores {lista_numeros}')
print(f'O maior valor digitado foi {max(lista_numeros)} nas posiçoes ', end='')
for c in range(0, len(posicao_maior)):
      print(f'{posicao_maior[c]}... ', end='')
print(f'\nO menor valor digitado foi {min(lista_numeros)} nas posiçoes ', end='')
for c in range(0, len(posicao_menor)):
        print(f'{posicao_menor[c]}... ', end='')
