# Aconfedereção Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date

vlAnoNascimento = int(input('Ano de dascimento: '))
vlAnoAtual = date.today().year
vlIdade = vlAnoAtual - vlAnoNascimento

print('O aluno tem {} anos '.format(vlIdade))
if vlIdade <= 9:
    print('Categoria : MIRIM')
elif vlIdade <= 14:
    print('Categoria : INFANTIL')
elif vlIdade <= 19:
    print('Categoria: JUNIOR')
elif vlIdade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')



