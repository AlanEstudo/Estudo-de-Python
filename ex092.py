# Crie um programa que leia o nome, ano de nascimento e carteira de trabalho
# Cadastre-os com a idade em um dicionário se por acaso a CTPS for diferente de zero,
# O dicionário receberá também o ano de contratação e o salario.
# Calcule  acrescente, além da idade, com quatos anos a pessoa vai se aposentar.

from datetime import datetime
dados = {}
dados["Nome"] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
dados["Idade"] = datetime.now().year - ano_nascimento
dados["Ctps"] = int(input('Carteira de Trabalho (0 não tem): '))
if dados["Ctps"] != 0:
    dados["Contratação"] = int(input('Ano de contratação: '))
    dados["Salário"] = float(input('Salário: R$'))
    dados["Aposentadoria"] = dados["Idade"] + ((dados["Contratação"] + 35) - datetime.now().year)
print('-=' * 40)
print(dados)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')

