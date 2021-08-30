# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

vlNota1 = float(input('Primeira nota: '))
vlNota2 = float(input('Segunda nota: '))
vlMedia = (vlNota1 + vlNota2) / 2

if vlMedia < 5.0:
    print('A média foi de {}, está abaixo de 5.0 REPROVADO! '.format(vlMedia))
elif vlMedia >= 5.0 and vlMedia <= 6.9:
    print('A média foi de {}, está entre 5.0 e 6.9 RECUPERAÇÃO '.format(vlMedia))
else:
    print('A média foi de {}, esta acima de 7.0 APROVADO '.format(vlMedia))
