# faça um programa que leia o ano de nascimento de uma jovem e informe, de acordo com sua idade:]
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

vlAnoNascimento = int(input('Qual o ano de nascimento: '))

vlAnoAtual = date.today().year
vlIdade = vlAnoAtual - vlAnoNascimento

if vlIdade < 18:
    print('Ainda vai se alistar!, faltam {} anos '.format(18 - vlIdade))
elif vlIdade == 18:
    print('Hora de se alistar!')
else:
    print('Passou do tempo, passou {} anos do prazo'.format(vlIdade - 18))


