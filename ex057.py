# faça um programa que leia o sexo de uma pessoa, mas ó aceite os valores 'M' ou 'F'.
# caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input('Informe seu sexo : [M]/[F]')).upper().strip()[0]
while sexo not in 'MmFf':
       sexo = str(input('Opção incorreta, tente novamente!!:')).strip().upper()[0]

print('Sexo {} registrado!'.format(sexo))



