# Faça um programa que leia o nome e média de um aluno.
# Quardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dados = {}
situacao = ''
dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input(f'Média da {dados["Nome"]}: '))

if dados["Media"] >= 6:
    situacao = 'Aprovado'
    dados["Situação"] = situacao
elif dados["Media"] >= 5 and dados["Media" < 6]:
    situacao = 'Recuperação'
    dados["Situação"] = situacao
else:
    situacao = 'Reprovado'
    dados["Situação"] = situacao

print('-=' * 40)
for k, v in dados.items():
    print(f' - {k} é iqual a {v}')

