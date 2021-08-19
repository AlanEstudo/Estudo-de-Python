# Escreva um programa que leia um valor em metros e exiba convertidos em centimetros e milimetros.

n = int(input('Digite um valor :'))
c = n * 100
m = n * 1000

print('Metros :{:.0f}\nCentimetros : {}\nMilimetros : {}'.format(n, c, m))