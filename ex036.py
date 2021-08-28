# Escreva um programa para aprovar o empréstimo bancário para a compra de um casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário ou então o empréstimo será negado

print('-' * 10 + ' Analise de Credito ' + '-' * 10)

vlValor = float(input('Valor da casa: '))
vlSalario = float(input('Valor do salário: '))
vlAnos = float(input('Quantos anos: '))

vlPrestacao = vlValor / (vlAnos * 12)
if vlPrestacao > vlSalario * 30 / 100:
    print('Empréstimo NEGADO!, o valor R${:.2f} ultrapassa 30 % do seu salario R$:{:.2f}'.format(vlPrestacao, vlSalario))
else:
    print('Valor da prestação mensal :R${:.2f}'.format(vlPrestacao))

print('-' * 10 + 'Anaslise conclúida ' + '-' * 10)
