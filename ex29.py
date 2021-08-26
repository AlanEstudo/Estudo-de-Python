# Escreve um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada km acima do limite

vlKm = float(input('Velocidade do carro: '))
vlAcima = vlKm - 80
vlCalculo = (vlKm - 80) * 7

if vlKm > 80:
    print('Você foi multado! O limite de velocidade é 80km/h e você esta {}km/h a cima da velocidade'.format(vlAcima))
    print('A multa vai custar R$7,00 por km ultrapassado,\nValor a pagar : R${:.2f}'.format(vlCalculo))
print('Tenha um bom dia! Digija com segurança!')