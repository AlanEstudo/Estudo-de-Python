# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar,
# considere U$$1.00 = R$:3,27

vlDinheiro = float(input('Valor em Real :'))

vlDolar = vlDinheiro * 3.27

print('Com {} reais voce pode comprar {:.2f} de dolares'.format(vlDinheiro, vlDolar))
