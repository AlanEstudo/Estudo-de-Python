#Tipos Primitivos e Saida de Dados

n1 = int(input('Digite o primeiro valor :'))
n2 = int(input('Digite o segundo valor :'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisao inteira é {} e potencia {}'.format(di, e))
