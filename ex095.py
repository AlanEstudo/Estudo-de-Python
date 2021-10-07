# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# depois vai ler a quantidade de gols feitos em cada partida.
# No final tudo isso vai ser quardado em um dicionario, incluindo o total de gols feitos durante o campeonato

# A primore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes o aproveitamento de cada jogador.

jogador = {}
partidas = list()
time = list()
while True:
    jogador.clear()
    print('-' * 35)
    jogador["Nome"] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador["Gols"] = partidas[:]
    jogador["Total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        sair = str(input('Quer continuar ? [S/N]')).upper()[0]
        if sair in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if sair == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Nostrar dados de qual jogador? (999 para parar!)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'   No jogo {i +1} fez {g} gols.')
    print('-' * 40)



