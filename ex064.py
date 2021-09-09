# Crie um programa que leia vários números inteiros pelo teclado.
# O programa so vai parar quando o usuário digitar o valor 999, que é a condição de para.
# No fial ,mostre quantos números foram digitados e qual foi a soma entre eles(Desconsidrando os flag)

sair = 0
cont = 0
soma = 0
sair = int(input('Digite um valor [999] para parar: '))
while sair != 999:
   cont += 1
   soma += sair
   sair = int(input('Digite um valor [999] para parar: '))
print('Foram digitados {} numeros.'.format(cont))
print('A soma entre os números digitados é {}.'.format(soma))
print('Fim do programa!!!')

