# Escreva um programa que leia um número inteiro qualquer e peça para o usúario escolher qual será a base de conversão
# 1 para Binario
# 2 para Octal
# 3 para Hexadecimal

vlNumero = int(input('Digite um número: '))
print('Base de conversão:\n[1]Binário\n[2]Octal\n[3]Hexadecimal')
vlOpcao = int(input('Sua opção:'))


if vlOpcao == 1:
    print('{} convertido para BINÁRIO é {}'.format(vlNumero, bin(vlNumero)))
elif vlOpcao == 2:
    print('{} convertido para OCTAL é {}'.format(vlNumero, oct(vlNumero)))
elif vlOpcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(vlNumero, hex(vlNumero)))
else:
    print('Opção INVÁLIDA!')
