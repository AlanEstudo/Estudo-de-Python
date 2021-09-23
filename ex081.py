# Crie um programa que vai ler vários números e colocar em uma lista.
# depois, mostre:
# Quantos números foram digitados
# A lista de valores ordenada por ordem descrecente.
# Se o valor 5 foi digitado e esta ou não na lista.

lista_numeros = []

while True:
    valor = int(input('Digite um valor: '))
    lista_numeros.append(valor)
    sair = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if sair in 'Nn':
        break
print('=-' * 30)
print(f'Foram digitados {len(lista_numeros)} números.')
lista_numeros.sort(reverse=True)
print(f'Os números digitados foram : {lista_numeros}')
if 5 in lista_numeros:
    print('O número 5 foi digitado, e esta na lista')
else:
    print('o numero 5 não foi digitado e não esta na lista')


