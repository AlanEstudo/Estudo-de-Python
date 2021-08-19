# Faça um algoritmo que leia o salario de um funcionario e moste seu novo salario, com 15% de aumento.

vlSalario = float(input('Qual o valor do salário? R$: '))

vlNovoSalario = vlSalario + (vlSalario * 15 / 100)

print('O novo Salário do fucionário com 15% e de R$:{}'.format(vlNovoSalario))