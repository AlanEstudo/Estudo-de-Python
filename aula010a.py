#Condição parte 1

vlNota1 = float(input('Digite a primeira nota: '))
vlNota2 = float(input('Digite a segunda nota: '))
vlMedia = (vlNota1 + vlNota2) / 2
print('A sua média foi {:.1f}'.format(vlMedia))
if vlMedia >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
