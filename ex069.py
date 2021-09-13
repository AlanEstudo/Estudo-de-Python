# Crie um programa que leia a idade eo sexo de várias pessoas.
# A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrado.
# Quantas mulheres tem menos de 20 anos.

pessoas_mais_18 = quantos_homens = mulheres_menos_20 = total = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]')).upper().strip()[0]

    total += 1
    if idade > 18:
        pessoas_mais_18 += 1
    if sexo == 'M':
        quantos_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar a cadastrar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('='*35)
print('Fim do programa!')
print('='*35)
print(f'Foram cadastrados {total} de pessoas !')
print(f'{pessoas_mais_18} Pessoas com mais de 18 anos.')
print(f'{quantos_homens} Homens cadastrados.')
print(f'{mulheres_menos_20} Mulheres com menos de 20 anos.')

