# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre sei status, de acardo com a tabela a baixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

vlPeso = float(input('Peso: '))
vlAltura = float(input('Altura: '))
vlImc= vlPeso / (vlAltura * vlAltura)

print('O IMC dessa pessoa é de {:.1f}'.format(vlImc))
if vlImc < 18.5:
    print('Abaixo do peso!')
elif vlImc >= 18.5 and vlImc < 25 :
    print('Peso ideal!')
elif vlImc >= 25 and vlImc < 30:
    print('Sobrepeso!')
elif vlImc >= 30 and vlImc < 40:
    print('Obesidade!')
else:
    print('Obesidade Mórbida')