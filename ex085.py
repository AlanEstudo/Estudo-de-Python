# Crie um programa onde o susuário posso difitar sete valores numéricos.
# Cadastre-os em uma lista única que matenha separados os valores pares e impares.
# No final mostra os valores pares e impares em ordem crescente.

numeros = [[], []]
valor = 0

for c in range(0, 7):
    valor = int(input(f'Digite o {c + 1}ª valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('=' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares foram {numeros[0]}')
print(f'Os valores impares foram {numeros[1]}')
