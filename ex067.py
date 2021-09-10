# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicita for negativo.

while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('='*35)
    if numero < 0:
        break
    for c in range(1, 10):
        print(f'{numero} x {c} = {numero * c}')
print('PROGRAMA TABUADA ENCERRADO!')
