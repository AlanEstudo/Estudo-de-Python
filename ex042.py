# Refaça o DESAFIO 035 os triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dos lados iguais
# Escalenso : todos os lados diferentes

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODE FORMAR trinângulo!')
    if r1 == r2 and r1 == r3:
       print('Equilátero: todos os lados iguais')
    elif r1 != r2 and r1 != r3 and r3 != r1:
        print('Escaleno:Todos os lados diferentes')
    else:
        print('Isósceles: Dois lados iguais')
else:
    print('Os segmentos a cima NAO PODEM FORMAR um triângulo')