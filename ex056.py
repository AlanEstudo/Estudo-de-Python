# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre :
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos

somaIdade = 0
mediaIade = 0
maisVelha = 0
nomeVelha = ''
menosIdade = 0
for c in range(1, 5):
    nome = str(input('Nome da {}º pessoa: '.format(c))).strip()
    idade = int(input('Idade da {}º pessoa: '.format(c)))
    sexo = int(input('Sexo da {}º pessoa: \n[1]MASCULINO\n[2]FEMININO\nOPÇÃO:'.format(c)))

    somaIdade += idade
    if c == 1 and sexo == 1:
        maisVelha = idade
        nomeVelha = nome
    if sexo == 1 and idade > maisVelha:
        maisVelha = idade
        nomeVelha = nome
    if sexo == 2 and idade < 20:
        menosIdade += 1
mediaIdade = somaIdade / 2

print('Média idade do grupo: {}'.format(mediaIdade))
print('Pessoa mais velha: {} com a idade de {}' .format(nomeVelha, maisVelha))
print('Mulheres com menos de 20 anos: {}'.format(menosIdade))

