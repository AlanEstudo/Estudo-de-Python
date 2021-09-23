# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois crie 2 lista extra que vão conter apenas os valores pares o os valores impares digitados.
# Ao final mostre o conteúdo das três listras geradas

lista_numeros= []
lista_impar = []
lista_par = []
while True:
    lista_numeros.append(int(input('Digite um valor: ')))
    sair = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if sair in 'N':
        break
for cont in range (0, len(lista_numeros)):
    if lista_numeros[cont] % 2 == 0:
        lista_par.append(lista_numeros[cont])
    else:
        lista_impar.append(lista_numeros[cont])
print('='*30)
print(f'Os valores digitados foram {lista_numeros}')
print(f'Os números PARES foram {lista_par}')
print(f'O números IMPARES foram {lista_impar}')

