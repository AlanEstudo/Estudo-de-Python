# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
# á vista dinheiro/cheque: 10% de desconto
# á vista no cartao: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

vlValorCusto = float(input('Valor a ser pago: '))

vlOpcao = int(input('-------- Opção de pagamento: -------------\n'
                    '[1] à vista dinheiro/chegue:10% de desconto!\n'
                    '[2] á vista no cartão: 5% de desconto!\n'
                    '[3] em até 2x no cartão: preço normal!\n'
                    '[4] 3x ou mais no cartão: 20% de juros\n'
                    'Opção:'))

if vlOpcao == 1:
    vlApagar = vlValorCusto - ((vlValorCusto * 10)/100)
    print('Valor a Pagar com 10% de desconto : R${:.2f}'.format(vlApagar))
elif vlOpcao == 2:
    vlApagar = vlValorCusto - ((vlValorCusto * 5) / 100)
    print('Valor a Pagar com 5% de desconto : R${:.2f}'.format(vlApagar))
elif vlOpcao == 3:
    print('Valor a pagar preço normal : R${:.2f}'.format(vlValorCusto))
elif vlOpcao == 4:
    vlApagar = vlValorCusto + ((vlValorCusto * 20) / 100)
    print('Valor a Pagar com 20% de juros : R${:.2f}'.format(vlApagar))
else:
    print('Opção incorreta! tente novamente...')
