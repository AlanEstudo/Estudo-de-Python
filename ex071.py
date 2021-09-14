# Crie um programa que simule o fucionamento de um caixa eletrônico.No inicio,
# Pergunte qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*30)
print('BANCO TOOSAQUE')
print('='*30)

valor_saque = int(input('Que valor você quer sacar? R$'))
total = valor_saque
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('=' * 30)