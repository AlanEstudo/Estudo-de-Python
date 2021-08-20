#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e RS0,15 por Km rodado

vlQntKm = int(input('Qual a quantidade em KM percorrido: '))
vlDiasUsado = int(input('Quantos dias usado: '))

#pago = (vlQntKm * 60 ) + (vlDiasUsado * 0.15)

vlValorDias = vlDiasUsado * 60
vlValorKm = vlQntKm * 0.15
vlCustoTotal = vlValorDias + vlValorKm
print('---- Resumo Fatura ----')
print('Valor de dias : R$:{}'.format(vlValorDias))
print('Valor do Km :RS:{} '.format(vlValorKm))
print('Total a Pagar RS:{}'.format(vlCustoTotal))