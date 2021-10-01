# Faça um programa que leia o nome e média de um aluno.
# Quardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dados = {}
situacao = ''
dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input(f'Média da {dados["Nome"]}: '))
print('-=' * 40)
print(f' - Nome é igual a {dados["Nome"]}.')
print(f' - Média é igual a {dados["Media"]}.')
if dados["Media"] >= 6:
    situacao = 'Aprovado'
    dados["Situação"] = situacao
elif dados["Media"] >= 5 and dados["Media" < 6]:
    situacao = 'Recuperação'
    dados["Situação"] = situacao
else:
    situacao = 'Reprovado'
    dados["Situação"] = situacao
print(f' - Situação é igual a {dados["Situação"]}')
