# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite a segunda nota :'))

m = (n1 + n2) / 2

print('A média entre {} e {} é iqual a {:.1f}'.format(n1, n2, m))