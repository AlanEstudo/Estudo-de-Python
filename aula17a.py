# Variáveis Compostas (Listas)

# .append(' ') => adiciona um elemento no final da lista
# .insert(0, ' ') => adiciona um elemento no inicio ou no indice da lista
# del variavel[3] => apaga o elemento na indice 3
# variavel.pop(3) => apaga o elemento no indice 2, caso não passa o indici apaga o ultimo elemento
# variavel.remove('item') => remove pelo valor da lista
# valores = list(range(4, 11)) => cria uma lista
# lista.sorte() => colocar em ordem os valores dentro da lista
# lista.sorte(reverse=True) => colocar os valores e orden decrescente
# len(lista) => saber quantos elementos tem na lista

#valores = []
#for cont in range(0, 5):
 #   valores.append(int(input('Digite um valor: ')))

#for c, v in enumerate(valores):
 #   print(f'Na posição {c} encontrei o valor {v} !')
#print('Cheguei no final da lista.')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'lista A: {a}')
print(f'lista B: {b}')