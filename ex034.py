# Escreva um programa que pergunte o salàrio de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiories ou iguais , o aumento é de 15%

vlSalario = float(input('Valor do salário: '))


if vlSalario > 1250:
    vlNovo = vlSalario + (vlSalario * 10 / 100)

else:
    vlNovo = vlSalario + (vlSalario * 15 / 100)

print('Quem ganha R${:.2f} passa a ganhar {:.2f} agora'.format(vlSalario, vlNovo))
