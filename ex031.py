# desenvolva um programa que pergunte a distância em uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0.50 por km para a viagens de até 200 km e R$0.45 para viagens mais longas

km = float(input('Qual a distância da viagem em Km: '))

print('------ Tabela de preço -------')
print('Até 200Km R$0.50 por Km ------')
print('Acima de 200Km R$0.45 por Km--')
print('--------Preço a pagar ! ------')
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print('Seu Km é de {}, valor a pagar :R${:.2f}'.format(km, preco))