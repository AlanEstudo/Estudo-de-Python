#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

vlPreco = float(input('Qual é o preço do produto ? R$ '))


vlNpreco = vlPreco - (vlPreco * 5 / 100)


print(' Preço novo do produto com 5% de desconto e de {:.2f} '.format(vlNpreco))