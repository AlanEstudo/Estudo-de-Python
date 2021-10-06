# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# E todos os dicionários em uma lista, no final mostre:
# Quantas pessoas foram cadastradas.
# A média de idade do grupo.
# Uma lista com todas as mulheres.
# Uma lista com idade a cima da média.

dados = list()
class_pessoa = dict()
media = soma = 0
while True:
    class_pessoa.clear()
    class_pessoa["nome"] = str(input('Nome: '))
    while True:
        class_pessoa["sexo"] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if class_pessoa["sexo"] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    class_pessoa["idade"] = int(input('Idade: '))
    soma += class_pessoa["idade"]
    dados.append(class_pessoa.copy())
    while True:
        sair = str(input('Quer continuar ? [S/N]')).upper()[0]
        if sair in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if sair == 'N':
        break
print('-=' * 40)
print(f'- O grupo tem {len(dados)} pessoas.')
media = soma / len(dados)
print(f'- A média de idade é de {media:5.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for pessoa in dados:
    if pessoa["sexo"] == 'F':
        print(f'{pessoa["nome"]} ', end='')
print()
print('Lista de pessoas que estão acima da média: ')
for pessoas in dados:
    if pessoas["idade"] > media:
        print(f'{pessoas}')


