# Crie um programa que leia o nome de uma pessoa completo e mostre:
# O nome com com todas as letras maiuscula
# O nome com todas as minusculas
# Quantas letras (sem considerar os espaços)
# Quantas letras tem o primeo nome

vlNome = str(input('Digite seu nome completo: ')).strip()
vlSepara = vlNome.split()
print('Letras Maiúscula: {}'.format(vlNome.upper()))
print('Letras Minuscula: {}'.format(vlNome.lower()))
print('Quantas letras sem os espaços: {}'.format(len(vlNome) - vlNome.count(' ')))
# print('Quantas letras tem o primeiro nome: {}'.format(vlNome.find(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(vlSepara[0], len(vlSepara[0])))