# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.No final mostre:
# quantas vezes apareceu o valor 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares.

numeros = (
    int(input('Digite um número: ')),
    int(input('Digite outro númeror: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))
)
print(f'Você digitou os valores{numeros}')
print(f'O numero 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}º posição')
else:
    print('O vaor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ',end=' ')
for c in numeros:
    if c % 2 == 0:
        print(c)
