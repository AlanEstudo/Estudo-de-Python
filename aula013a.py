# Estrutura de repetição

'''n = int(input('Digite um numro: '))
for c in range(0, n+1, 2):
    print(c)
print('Fim')'''

'''i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i,f + 1, p ):
    print(c)
print('FIM')'''

'''for c in range(0, 3):
    n = int(input('Digite um numero: '))
print('FIM')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite  um valor: '))
    s += n
print('A soma de todos os valores é de :{}'.format(s))